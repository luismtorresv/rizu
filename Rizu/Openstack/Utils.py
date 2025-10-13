import openstack


class OpenStackUtils:

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
    def assign_openstack_role(project_name, username, role, conn_token):
        project = conn_token.identity.find_project(project_name, domain_id="Default")
        user = conn_token.identity.find_user(username, domain_id="Default")
        project_role = conn_token.identity.find_role(role)

        if not project or not user or not project_role:
            raise ValueError("Project, user, or role not found")

        # DEBUG: show all assignments for this user
        assignments = list(
            conn_token.identity.role_assignments(
                user_id=user.id,
                include_names=True,
            )
        )
        
        # for a in assignments:
        #     print("ASSIGNMENT:", a.scope, a.role["name"])

        # Check if user already has this role on the project
        existing_roles = set()
        for a in assignments:
            scope = a.scope
            #  only roles directly assigned to this project count
            if "project" in scope and scope["project"]["id"] == project.id:
                existing_roles.add(a.role["name"].lower())

        # print(f"[DEBUG] Project: {project.name} ({project.id})")
        # print(f"[DEBUG] Roles found: {existing_roles}")

        # Only assign if it’s not already there
        if role.lower() not in existing_roles:
            conn_token.identity.assign_project_role_to_user(project, user, project_role)
            print(f"[INFO] Assigned {role} to {username} in {project.name}")
        else:
            print(f"[INFO] {username} already has {role} in {project.name}")

        # Optional: handle default project if necessary
        if role.lower() == "member" and not getattr(user, "default_project_id", None):
            conn_token.identity.update_user(user, default_project_id=project.id)

    @staticmethod
    def get_user_primary_role(openstack_user, project_id, conn_token):
        try:
            # Fetch only role assignments for this user in this project
            assignments = list(
                conn_token.identity.role_assignments(
                    user_id=openstack_user.id,
                    project_id=project_id,
                    include_names=True,  # critical fix
                    scope_type="project",
                )
            )

            if not assignments:
                return "No relevant role assigned"

            # Extract role names safely
            role_names = [
                a.role["name"].lower()
                for a in assignments
                if "name" in a.role
                and a.scope.get("project", {}).get("id") == project_id
            ]

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
