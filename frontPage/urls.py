from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create-vm/", views.create_vm, name="create_vm"),  # ruta de crear vm
    path("create-project/", views.create_project, name="create_project"),
]
