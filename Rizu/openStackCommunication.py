import openstack
import os


class OpenStackCommunication:
    def __init__(self, cloud="kolla-admin-system"):
        self.conn = openstack.connect(cloud=cloud)

    def create_openstack_project(self, project_name, project_description, user, role):
        try:
            new_project = self.conn.identity.create_project(
                name=project_name,
                description=project_description,
                domain_id="default",
                enabled=True,
            )

            # assign myself to the project
            self.assign_openstack_role(project_name, user.username, role)

            return True
        except Exception as e:
            print(f"Something went wrong with the project creation. Error: {e}")
            return False

    def create_openstack_user(self, user):
        new_user = self.conn.identity.create_user(
            name=user.username,
            password=user.password,
            domain_id="default",
            email=user.email,
            default_project_id=None,  # or specify a project ID if needed
            enabled=True,
        )

    def assign_openstack_role(self, project_name, username, role):
        project = self.conn.identity.find_project(project_name)
        user = self.conn.identity.find_user(username)
        project_role = self.conn.identity.find_role(role)

        if not project:
            raise ValueError(f"❌ Project '{project_name}' not found in OpenStack.")

        if not user:
            raise ValueError(f"❌ User '{username}' not found in OpenStack.")

        if not project_role:
            raise ValueError(f"❌ Role '{role}' not found in OpenStack.")

        self.conn.identity.assign_project_role_to_user(project, user, project_role)

    def create_openstack_network(self, network_name, project_id):
        try:
            # Connect directly with project scope
            conn = openstack.connect(cloud="kolla-admin", project_id=project_id)

            network = conn.network.create_network(
                name=network_name,
                project_id=project_id,
                is_router_external=False,
                admin_state_up=True,
            )
            return network
        except Exception as e:
            print(f"Failed to create network {network_name}: {e}")
            return None

    def create_openstack_router(
        self, router_name, project_id, external_network_name=None
    ):
        try:
            # Connect directly with project scope
            conn = openstack.connect(cloud="kolla-admin", project_id=project_id)

            kwargs = {
                "name": router_name,
                "project_id": project_id,
                "admin_state_up": True,
            }

            if external_network_name:
                ext_net = conn.network.find_network(
                    external_network_name, external=True
                )
                if not ext_net:
                    raise ValueError(
                        f"External network {external_network_name} not found"
                    )
                kwargs["external_gateway_info"] = {"network_id": ext_net.id}

            router = conn.network.create_router(**kwargs)
            return router
        except Exception as e:
            print(f"Failed to create router {router_name}: {e}")
            return None
