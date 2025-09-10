from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("networks/create/", views.create_network, name="create_network"),
    path("routers/create/", views.create_router, name="create_router"),
    path("vms/create/", views.create_vm, name="create_vm"),  # placeholder
    path("create-vm/", views.create_vm, name="create_vm"),  # ruta de crear vm
    path("create-project/", views.create_project, name="create_project"),  # ruta de crear project
]
