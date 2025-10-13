import openstack
import secrets
import string


class OpenStackCommunication:
    @staticmethod
    def get_connection(request=None, project_id=None, system=False):
        try:
            if system:
                return openstack.connect(cloud="kolla-admin-system")

            if request and hasattr(request, "user") and request.user.is_authenticated:
                if project_id:
                    # Project-scoped token for managers or members
                    return openstack.connect(
                        auth=dict(
                            username=request.user.username,
                            password=request.user.openstack_password,
                            project_id=project_id,
                            auth_url="http://192.168.10.254:5000/v3",
                            user_domain_name="Default",
                            project_domain_name="Default",
                        )
                    )
                else:
                    # fallback: system token for listing projects
                    return openstack.connect(
                        auth=dict(
                            username=request.user.username,
                            password=request.user.openstack_password,
                            auth_url="http://192.168.10.254:5000/v3",
                            user_domain_name="Default",
                        )
                    )

            # fallback generic
            return openstack.connect(cloud="kolla-admin")
        except Exception as e:
            print(f"Cannot connect to Openstack. Error: {e}")
            return

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

            OpenStackCommunication.assign_openstack_role(
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
            rand_pass = OpenStackCommunication.generate_password()  # OpenStack Password

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
    def assign_openstack_role(project_name, username, role, conn_token):
        project = conn_token.identity.find_project(project_name)
        user = conn_token.identity.find_user(username)
        project_role = conn_token.identity.find_role(role)

        if not project:
            raise ValueError(f" Project '{project_name}' not found in OpenStack.")
        if not user:
            raise ValueError(f" User '{username}' not found in OpenStack.")
        if not project_role:
            raise ValueError(f" Role '{role}' not found in OpenStack.")

        # Check if user already has this role on the project
        existing_roles = [
            r.role["name"].lower()
            for r in conn_token.identity.role_assignments(
                user_id=user.id, project_id=project.id, include_names=True
            )
            if "name" in r.role
        ]

        if role.lower() in existing_roles:
            print(
                f" User {username} already has role '{role}' in project '{project_name}', skipping assignment."
            )
            return

        # Only assign if it’s not already there
        conn_token.identity.assign_project_role_to_user(project, user, project_role)

        # Optional: handle default project if necessary
        if role == "member":
            if (
                not getattr(user, "default_project_id", None)
                or user.default_project_id != project.id
            ):
                conn_token.identity.update_user(user, default_project_id=project.id)

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

    @staticmethod
    def get_user_primary_role(openstack_user, project_id, conn_token):
        try:
            # Fetch only role assignments for this user in this project
            assignments = list(
                conn_token.identity.role_assignments(
                    user_id=openstack_user.id,
                    project_id=project_id,
                    include_names=True,  # critical fix
                )
            )

            if not assignments:
                return "No relevant role assigned"

            # Extract role names safely
            role_names = [
                a.role["name"].lower() for a in assignments if "name" in a.role
            ]

            print(f"Roles for {openstack_user.name} in {project_id}: {role_names}")

            # Priority: admin > project_manager > member
            if "admin" in role_names:
                return "admin"
            elif "project_manager" in role_names:
                return "project_manager"
            elif "member" in role_names:
                return "member"
            else:
                return "No relevant role assigned"

        except Exception as e:
            print(f"Error fetching user role for {openstack_user.name}: {e}")
            return "Error retrieving role"
