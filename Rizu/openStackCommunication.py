import openstack
import os


class OpenStackCommunication:
    def __init__(self, cloud="kolla-admin-system"):
        os.environ["OS_CLIENT_CONFIG_FILE"] = os.path.expanduser(
            "/etc/kolla/clouds.yaml"
        )
        self.conn = openstack.connect(cloud=cloud)

    def create_openstack_project(self, project_name, project_description, username):
        try:
            new_project = self.conn.identity.create_project(
                name=project_name,
                description=project_description,
                domain_id="default",
                enabled=True,
            )

            # assign myself to the project
            self.assign_openstack_role(project_name, username)

            return True
        except Exception as e:
            print(f"Something went wrong with the project creation. Error: {e}")
            return False

    def assign_openstack_role(self, project_name, username):
        project = self.conn.identity.find_project(project_name)
        user = self.conn.identity.find_user(username)
        role = self.conn.identity.find_role("admin")

        if not (project and user and role):
            raise ValueError("Project, user, or role not found!")

        self.conn.identity.assign_project_role_to_user(project, user, role)

    def create_openstack_network(self, network_name, project_name):
        try:
            project = self.conn.identity.find_project(project_name)
            if not project:
                raise ValueError(f"Project {project_name} not found")

            # create network
            network = self.conn.network.create_network(
                name=network_name,
                project_id=project.id,
                is_router_external=False,
                admin_state_up=True,
            )
            return network
        except Exception as e:
            print(f"Failed to create network {network_name}: {e}")
            return None

    def create_openstack_router(
        self, router_name, project_name, external_network_name=None
    ):
        try:
            project = self.conn.identity.find_project(project_name)
            if not project:
                raise ValueError(f"Project {project_name} not found")

            kwargs = {
                "name": router_name,
                "project_id": project.id,
                "admin_state_up": True,
            }

            # optionally set gateway if you pass an external network
            if external_network_name:
                ext_net = self.conn.network.find_network(
                    external_network_name, external=True
                )
                if not ext_net:
                    raise ValueError(
                        f"External network {external_network_name} not found"
                    )
                kwargs["external_gateway_info"] = {"network_id": ext_net.id}

            router = self.conn.network.create_router(**kwargs)
            return router
        except Exception as e:
            print(f"Failed to create router {router_name}: {e}")
            return None
