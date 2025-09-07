import openstack
import os

class openStackCommunication:

    os.environ['OS_CLIENT_CONFIG_FILE'] = os.path.expanduser('/etc/kolla/clouds.yaml')
    conn = openstack.connect(cloud='kolla-admin-system')
    

    def create_Openstack_Project(self, project_name, project_description):
        try: 

            new_project = self.conn.identity.create_project(
                name = project_name,
                description = project_description,
                domain_id = 'default',
                enabled = True,
            )

            return 0
        except:

            return 1
            print('Something went wrong with the project creation')
