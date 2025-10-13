from Rizu.Openstack.Utils import OpenStackUtils
import secrets
import string


class OpenStackBuilders:

    @staticmethod
    def create_openstack_project(
        project_name, project_description, user, role, conn_token
    ):
        try:
            _ = conn_token.identity.create_project(
                name=project_name,
                description=project_description,
                domain_id="default",
                enabled=True,
            )

            # assign myself to the project

            OpenStackUtils.assign_openstack_role(
                project_name, user.username, role, conn_token
            )

            return True
        except Exception as e:
            print(f"Something went wrong with the project creation. Error: {e}")
            return False

    @staticmethod
    def generate_password(length=16):
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(length))

    @staticmethod
    def create_openstack_user(user, conn_token):
        try:
            rand_pass = OpenStackBuilders.generate_password()  # OpenStack Password

            _ = conn_token.identity.create_user(
                name=user.username,
                password=rand_pass,
                domain_id="default",
                email=user.email,
                default_project_id=None,  # or specify a project ID if needed
                enabled=True,
            )

            user.openstack_password = rand_pass
            user.save()
        except Exception as e:
            print(f"Something went wrong with the user creation process. Error: {e}")
            return False

    @staticmethod
    def create_openstack_network(network_name, project_id, conn_token):
        try:
            # Connect directly with project scope

            network = conn_token.network.create_network(
                name=network_name,
                project_id=project_id,
                is_router_external=False,
                admin_state_up=True,
            )
            return network
        except Exception as e:
            print(f"Failed to create network {network_name}: {e}")
            return None

    @staticmethod
    def create_openstack_router(
        router_name,
        project_id,
        conn_token,
        external_network_name=None,
    ):
        try:
            kwargs = {
                "name": router_name,
                "project_id": project_id,
                "admin_state_up": True,
            }

            if external_network_name:
                ext_net = conn_token.network.find_network(
                    external_network_name, external=True
                )
                if not ext_net:
                    raise ValueError(
                        f"External network {external_network_name} not found"
                    )
                kwargs["external_gateway_info"] = {"network_id": ext_net.id}

            router = conn_token.network.create_router(**kwargs)
            return router
        except Exception as e:
            print(f"Failed to create router {router_name}: {e}")
            return None
