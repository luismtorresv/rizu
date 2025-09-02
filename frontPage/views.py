from django.shortcuts import render

def dashboard(request):

    # Datos falsos de ejemplo 
    resources = {
        'vms': [
            {'name': 'fisher', 'type': 'VM instance', 'status': 'Running'},
            {'name': 'johnson', 'type': 'VM instance', 'status': 'Stopped'},
        ],
        'load_balancers': [
            {'name': 'kellner', 'type': 'Load balancer', 'status': 'Active'},
        ],
        'databases': [
            {'name': 'melina', 'type': 'Database', 'status': 'Available'},
        ]
    }

    user_info = {
        'subnet': 'X.X.X.X/8',
        'status': 'Running',
        'current_account': 'Elias',
        'role': 'Admin'
    }

    context = {
        'resources': resources,
        'user_info': user_info,
    }

    return render(request, 'dashboard.html', context)

def create_vm(request):
    return render(request, 'create_vm.html') 