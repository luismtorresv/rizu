import openstack
import os


class OpenStackCommunication:

    os.environ["OS_CLIENT_CONFIG_FILE"] = os.path.expanduser("/etc/kolla/clouds.yaml")
    conn = openstack.connect(cloud="kolla-admin-system")

    def create_openstack_project(self, project_name, project_description):
        try:

            new_project = self.conn.identity.create_project(
                name=project_name,
                description=project_description,
                domain_id="default",
                enabled=True,
            )

            return True
        except:

            return False
            print("Something went wrong with the project creation")
