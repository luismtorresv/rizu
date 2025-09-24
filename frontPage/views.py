from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import openstack
import os


from Rizu.openStackCommunication import OpenStackCommunication

osc = OpenStackCommunication()


def get_connection(project_id=None, system=False):
    os.environ["OS_CLIENT_CONFIG_FILE"] = os.path.expanduser("/etc/kolla/clouds.yaml")

    if system:
        return openstack.connect(cloud="kolla-admin-system")

    if project_id:
        return openstack.connect(cloud="kolla-admin", project_id=project_id)

    return openstack.connect(cloud="kolla-admin")


def dashboard(request):
    project_id = request.GET.get("project_id")

    sys_conn = get_connection(system=True)
    projects = [
        {"id": proj.id, "name": proj.name, "description": proj.description}
        for proj in sys_conn.identity.projects()
        if proj.name.lower() not in ["service", "services"]
    ]

    selected_project = None
    resources = {"instances": [], "routers": [], "networks": []}

    if project_id:
        conn = get_connection(project_id=project_id)
        request.session["project_id"] = project_id
        selected_project = conn.identity.get_project(project_id)

        try:
            resources["instances"] = [vm.to_dict() for vm in conn.compute.servers()]
        except Exception as e:
            print(f"Error listing instances: {e}")

        try:
            resources["routers"] = [
                router.to_dict() for router in conn.network.routers()
            ]
        except Exception as e:
            print(f"Error listing routers: {e}")

        try:
            resources["networks"] = [
                net.to_dict()
                for net in conn.network.networks()
                if net.project_id == project_id
            ]
        except Exception as e:
            print(f"Error listing networks: {e}")

        try:
            current_account = conn.current_user.name
        except Exception:
            current_account = "N/A"

        # Roles in the project
        roles = []
        try:
            roles = [
                role.name
                for role in conn.identity.roles(
                    user=conn.current_user_id, project=project_id
                )
            ]
        except Exception as e:
            print(f"Error getting roles: {e}")
        role_info = ", ".join(roles) if roles else "N/A"

    user_info = None
    if selected_project:
        user_info = {
            "project_id": selected_project.id,
            "project_name": selected_project.name,
            "status": "Enabled" if selected_project.is_enabled else "Disabled",
            "instances": len(resources["instances"]),
            "routers": len(resources["routers"]),
            "networks": len(resources["networks"]),
            "role": role_info,
        }

    context = {
        "projects": projects,
        "selected_project": (
            {
                "id": selected_project.id if selected_project else None,
                "name": selected_project.name if selected_project else None,
                "description": (
                    selected_project.description if selected_project else None
                ),
                "resources": resources,
            }
            if selected_project
            else None
        ),
        "user_info": user_info,
    }

    return render(request, "dashboard.html", context)


def create_vm(request):
    return render(request, "create_vm.html")


def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        username = "admin"  # you can change this later based on real authentication

        conn = OpenStackCommunication()
        response = conn.create_openstack_project(name, description, username)

        # Show response or redirect to dashboard
        if response is False:
            return HttpResponse("Error")  # failure

        return HttpResponse("Success")  # success

    # If it's GET, just render the form
    return render(request, "create_project.html")


def create_network(request):
    if request.method == "POST":
        name = request.POST.get("network_name")
        project_id = request.session.get("project_id")
        net = osc.create_openstack_network(name, project_id)
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
