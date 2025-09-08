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
