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



