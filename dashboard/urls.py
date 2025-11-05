from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("networks/create/", views.create_network, name="create_network"),
    path("routers/create/", views.create_router, name="create_router"),
    path("vms/create/", views.create_vm, name="create_vm"),  # placeholder
    path("create-vm/", views.create_vm, name="create_vm"),  # ruta de crear vm
    path(
        "create-project/", views.create_project, name="create_project"
    ),  # ruta de crear project
    path(
        "projects/join/", views.join_projects_view, name="join_projects"
    ),  # ruta de join projects
    path(
        "projects/<str:project_id>/", views.project_detail_view, name="project_detail"
    ),
    path("terraform/", views.terraform_view, name="terraform"),
    path("user/profile/", views.user_profile, name="user_profile"),
    path("storage/create/", views.create_storage, name="create_storage"),
]
