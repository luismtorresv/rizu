from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import openstack
import os


from Rizu.openStackCommunication import OpenStackCommunication

osc = OpenStackCommunication()


def get_connection(request=None, project_id=None, system=False):
    if system:
        return openstack.connect(cloud="kolla-admin-system")

    if request and hasattr(request, "user") and request.user.is_authenticated:
        if project_id:
            # Project-scoped token for managers or members
            return openstack.connect(
                auth=dict(
                    username=request.user.username,
                    password=request.user.openstack_password,
                    project_id=project_id,
                    auth_url="http://192.168.10.254:5000/v3",
                    user_domain_name="Default",
                    project_domain_name="Default",
                )
            )
        else:
            # fallback: system token for listing projects
            return openstack.connect(
                auth=dict(
                    username=request.user.username,
                    password=request.user.openstack_password,
                    auth_url="http://192.168.10.254:5000/v3",
                    user_domain_name="Default",
                )
            )

    # fallback generic
    return openstack.connect(cloud="kolla-admin")


def dashboard(request):
    project_id = request.GET.get("project_id")
    user = request.user

    # Admin/system connection (has full visibility
    conn = get_connection(system=True)

    # Filter projects depending on user role
    if user.role == "admin":
        # Admins see all non-service projects
        projects = [
            {"id": proj.id, "name": proj.name, "description": proj.description}
            for proj in conn.identity.projects()
            if proj.name.lower() not in ["service", "services"]
        ]

    elif user.role == "project_manager":
        # Managers see only projects they own
        # (Assuming you tagged projects with "owner:<username>" or similar)
        projects = [
            {"id": proj.id, "name": proj.name, "description": proj.description}
            for proj in conn.identity.projects()
            if getattr(proj, "tags", []) and f"owner:{user.username}" in proj.tags
        ]

    elif user.role == "member":
        # Members see projects they belong to
        projects = [
            {"id": p.id, "name": p.name, "description": p.description}
            for p in conn.identity.projects(user=conn.current_user_id)
        ]

    else:
        # Default fallback (guest / no role)
        projects = []

    selected_project_obj = None
    resources = {"instances": [], "routers": [], "networks": [], "volumes": []}

    if project_id:
        conn = get_connection(request=request, project_id=project_id)
        request.session["project_id"] = project_id
        try:
            selected_project_obj = conn.identity.get_project(project_id)
        except Exception as e:
            print(f"Failed to fetch selected project: {e}")
            selected_project_obj = None

    if selected_project_obj:
        # Instances
        try:
            resources["instances"] = [vm.to_dict() for vm in conn.compute.servers()]
        except Exception as e:
            print(f"Error listing instances: {e}")

        # Routers
        try:
            resources["routers"] = [r.to_dict() for r in conn.network.routers()]
        except Exception as e:
            print(f"Error listing routers: {e}")

        # Networks
        try:
            resources["networks"] = [
                n.to_dict()
                for n in conn.network.networks()
                if getattr(n, "project_id", None) == project_id
            ]
        except Exception as e:
            print(f"Error listing networks: {e}")

        # Volumes (optional but shown in the template)
        try:
            # Depending on SDK/permissions you may need details=True/False
            resources["volumes"] = [
                v.to_dict()
                for v in conn.block_storage.volumes()
                if getattr(v, "project_id", None) == project_id
            ]
        except Exception as e:
            print(f"Error listing volumes: {e}")

        # Current account (not required, but kept if you use it elsewhere)
        try:
            current_account = conn.current_user.name
        except Exception:
            current_account = "N/A"

    user_info = None
    if selected_project_obj:
        user_info = {
            "project_id": selected_project_obj.id,
            "project_name": selected_project_obj.name,
            "status": "Enabled" if selected_project_obj.is_enabled else "Disabled",
            "instances": len(resources["instances"]),
            "routers": len(resources["routers"]),
            "networks": len(resources["networks"]),
            "volumes": len(resources["volumes"]),
        }

    context = {
        "projects": projects,
        "selected_project": (
            {
                "id": selected_project_obj.id,
                "name": selected_project_obj.name,
                "description": selected_project_obj.description,
                "resources": resources,
            }
            if selected_project_obj
            else None
        ),
        "user_info": user_info,
    }

    return render(request, "dashboard.html", context)


def create_vm(request):
    return render(request, "create_vm.html")


def create_project(request):
    if request.user.role != "project_manager":
        return HttpResponse("You are not allowed to create projects.")

    osc = OpenStackCommunication("kolla-admin-system")

    if request.method == "POST":
        project_name = request.POST.get("name")
        description = request.POST.get("description")

        # Ensure these fields exist
        if not project_name:
            return HttpResponse("Project name is required.", status=400)

        user = request.user  # puedes cambiarlo luego según autenticación real
        user_role = user.role

        response = osc.create_openstack_project(
            project_name, description, user, user_role
        )

        # Muestras respuesta o rediriges al dashboard
        if not response:
            return HttpResponse("Error creating project", status=500)

        return redirect("dashboard")

    # Si es GET, solo renderizas el formulario
    return render(request, "create_project.html")


def create_network(request):
    if request.method == "POST":

        name = request.POST.get("network_name")
        project_id = request.session.get("project_id")

        # Give temporary admin-level credentials
        conn = get_connection(request=request, project_id=project_id)

        net = osc.create_openstack_network(name, project_id, conn)

        if net:
            messages.success(request, f"Network {name} created")
        else:
            messages.error(request, "Failed to create network")
        return redirect("dashboard")
    return render(request, "create_network.html")


def create_router(request):
    if request.method == "POST":
        name = request.POST.get("router_name")
        project_id = request.session.get("project_id")
        external_net = request.POST.get("external_network_name") or None
        router = osc.create_openstack_router(name, project_id, external_net)

        if router:
            messages.success(request, f"Router {name} created")
        else:
            messages.error(request, "Failed to create router")
        return redirect("dashboard")
    return render(request, "create_router.html")


# -------- JOIN PROJECTS AND PROJECT DETAIL VIEWS (no terminado..)--------
def _initials(name: str) -> str:
    if not name:
        return "PR"
    parts = [p for p in name.strip().split() if p]
    return (parts[0][0] + (parts[1][0] if len(parts) > 1 else "")).upper()


def join_projects_view(request):
    q = (request.GET.get("q") or "").strip().lower()

    try:
        sys_conn = get_connection(system=True)
        projects_raw = [
            {"id": p.id, "name": p.name, "description": p.description or ""}
            for p in sys_conn.identity.projects()
            if p.name and p.name.lower() not in ["service", "services"]
        ]
    except Exception:
        projects_raw = []

    projects = []
    for p in projects_raw:
        if q and q not in f"{p['name']} {p['description']}".lower():
            continue
        p["initials"] = _initials(p["name"])
        projects.append(p)

    projects.sort(key=lambda x: x["name"].lower())

    username = (
        request.user.get_full_name() or request.user.get_username()
        if request.user.is_authenticated
        else "Guest"
    )

    return render(
        request,
        "join_projects.html",
        {
            "projects": projects,
            "request": request,
            "username": username,
        },
    )


def project_detail_view(request, project_id: str):
    conn = get_connection(request=request, project_id=project_id)
    project = conn.identity.get_project(project_id)

    resources = {"instances": [], "routers": [], "networks": []}
    try:
        resources["instances"] = [vm.to_dict() for vm in conn.compute.servers()]
    except Exception:
        pass
    try:
        resources["routers"] = [r.to_dict() for r in conn.network.routers()]
    except Exception:
        pass
    try:
        resources["networks"] = [
            n.to_dict()
            for n in conn.network.networks()
            if getattr(n, "project_id", None) == project_id
        ]
    except Exception:
        pass

    context = {
        "project": {
            "id": project.id,
            "name": project.name,
            "description": project.description or "",
        },
        "resources": resources,
    }
    return render(request, "project_detail.html", context)
