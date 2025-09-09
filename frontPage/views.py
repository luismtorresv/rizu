from django.shortcuts import render
from django.http import HttpResponse

from Rizu.openStackCommunication import OpenStackCommunication


def dashboard(request):
    # Datos falsos de ejemplo
    resources = {
        "vms": [
            {"name": "fisher", "type": "VM instance", "status": "Running"},
            {"name": "johnson", "type": "VM instance", "status": "Stopped"},
        ],
        "load_balancers": [
            {"name": "kellner", "type": "Load balancer", "status": "Active"},
        ],
        "databases": [
            {"name": "melina", "type": "Database", "status": "Available"},
        ],
    }

    user_info = {
        "subnet": "X.X.X.X/8",
        "status": "Running",
        "current_account": "Elias",
        "role": "Admin",
    }

    context = {
        "resources": resources,
        "user_info": user_info,
    }

    return render(request, "dashboard.html", context)


def create_vm(request):
    return render(request, "create_vm.html")


def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        username = "admin"  # puedes cambiarlo luego según autenticación real

        conn = OpenStackCommunication()
        response = conn.create_openstack_project(name, description, username)

        # Muestras respuesta o rediriges al dashboard
        if response is False:
            return HttpResponse("Error")   # fallo
        
        return HttpResponse("Funciono") # éxito

        
    

    # Si es GET, solo renderizas el formulario
    return render(request, "create_project.html")