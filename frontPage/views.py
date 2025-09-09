from django.shortcuts import render
from django.http import HttpResponse
import openstack
import os

from Rizu.openStackCommunication import OpenStackCommunication


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
    proyectos = [
        {"id": proj.id, "nombre": proj.name, "descripcion": proj.description}
        for proj in sys_conn.identity.projects()
        if proj.name.lower() not in ["service", "services"]
]

    proyecto_seleccionado = None
    recursos = {"instancias": [], "routers": [], "redes": []}


    if project_id:
        
        conn = get_connection(project_id=project_id)
        proyecto_seleccionado = conn.identity.get_project(project_id)

        try:
            recursos["instancias"] = [vm.to_dict() for vm in conn.compute.servers()]
        except Exception as e:
            print(f"Error al listar instancias: {e}")

        try:
            recursos["routers"] = [router.to_dict() for router in conn.network.routers()]
        except Exception as e:
            print(f"Error al listar routers: {e}")

        try:
            recursos["redes"] = [net.to_dict() for net in conn.network.networks() if net.project_id == project_id]
        except Exception as e:
            print(f"Error al listar redes: {e}")

        try:
            current_account = conn.current_user.name
        except Exception:
            current_account = "N/A"

        # Roles en el proyecto
        roles = []
        try:
            roles = [
                role.name
                for role in conn.identity.roles(
                    user=conn.current_user_id,
                    project=project_id
                )
            ]
        except Exception as e:
            print(f"Error al obtener roles: {e}")
        role_info = ", ".join(roles) if roles else "N/A"

    user_info = None
    if proyecto_seleccionado:
        user_info = {
            "project_id": proyecto_seleccionado.id,
            "project_name": proyecto_seleccionado.name,
            "status": "Enabled" if proyecto_seleccionado.is_enabled else "Disabled",
            "instances": len(recursos["instancias"]),
            "routers": len(recursos["routers"]),
            "networks": len(recursos["redes"]),
            "role": role_info,
        }

    context = {
        "proyectos": proyectos,
        "proyecto_seleccionado": {
            "id": proyecto_seleccionado.id if proyecto_seleccionado else None,
            "nombre": proyecto_seleccionado.name if proyecto_seleccionado else None,
            "descripcion": proyecto_seleccionado.description if proyecto_seleccionado else None,
            "recursos": recursos,
        } if proyecto_seleccionado else None,
        "user_info": user_info,  
    }

    return render(request, "dashboard.html", context)

def create_vm(request):
    return render(request, "create_vm.html")


def create_project(request):
    test_name = "project 1"
    test_description = "this is the first test project for Rizu. Let's pray it works"
    test_username = "admin"

    conn = OpenStackCommunication()
    response = conn.create_openstack_project(test_name, test_description, test_username)

    print(response)

    return HttpResponse(
        "this is the first test project for Rizu. Let's pray it works",
        content_type="text/plain",
    )


