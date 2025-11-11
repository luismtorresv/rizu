"""
Mock OpenStack Utils for Testing

This module provides mock implementations of OpenStack utilities that don't
require actual OpenStack connections. Used for testing when VPN/network
access to OpenStack is not available.
"""

from typing import Any, Dict, List, Optional
import uuid
import random


class MockProject:
    """Mock OpenStack project object"""

    def __init__(self, name: str, description: str = "", project_id: str = None):
        self.id = project_id or str(uuid.uuid4())
        self.name = name
        self.description = description
        self.enabled = True
        self.domain_id = "default"


class MockUser:
    """Mock OpenStack user object"""

    def __init__(self, username: str, email: str = "", user_id: str = None):
        self.id = user_id or str(uuid.uuid4())
        self.name = username
        self.username = username
        self.email = email
        self.enabled = True
        self.domain_id = "default"


class MockNetwork:
    """Mock OpenStack network object"""

    def __init__(self, name: str, network_id: str = None):
        self.id = network_id or str(uuid.uuid4())
        self.name = name
        self.admin_state_up = True
        self.is_router_external = False
        self.status = "ACTIVE"
        self.subnet_ids = [str(uuid.uuid4())]


class MockSubnet:
    """Mock OpenStack subnet object"""

    def __init__(self, name: str, cidr: str = "10.0.0.0/24", subnet_id: str = None):
        self.id = subnet_id or str(uuid.uuid4())
        self.name = name
        self.cidr = cidr
        self.ip_version = 4
        self.enable_dhcp = True
        self.gateway_ip = "10.0.0.1"


class MockRouter:
    """Mock OpenStack router object"""

    def __init__(self, name: str, router_id: str = None):
        self.id = router_id or str(uuid.uuid4())
        self.name = name
        self.admin_state_up = True
        self.status = "ACTIVE"
        self.external_gateway_info = None


class MockFlavor:
    """Mock OpenStack compute flavor"""

    def __init__(self, name: str, flavor_id: str = None):
        self.id = flavor_id or str(uuid.uuid4())
        self.name = name
        self.vcpus = random.choice([1, 2, 4])
        self.ram = random.choice([1024, 2048, 4096])
        self.disk = random.choice([20, 40, 80])


class MockImage:
    """Mock OpenStack image"""

    def __init__(self, name: str, image_id: str = None):
        self.id = image_id or str(uuid.uuid4())
        self.name = name
        self.status = "ACTIVE"
        self.os_distro = random.choice(["ubuntu", "centos", "debian"])


class MockInstance:
    """Mock OpenStack compute instance"""

    def __init__(self, name: str, instance_id: str = None):
        self.id = instance_id or str(uuid.uuid4())
        self.name = name
        self.status = "ACTIVE"
        self.addresses = {
            "private-network": [
                {
                    "addr": f"10.0.0.{random.randint(10, 100)}",
                    "OS-EXT-IPS:type": "fixed",
                },
                {
                    "addr": f"192.168.1.{random.randint(10, 100)}",
                    "OS-EXT-IPS:type": "floating",
                },
            ]
        }
        self.flavor = {"id": str(uuid.uuid4())}
        self.image = {"id": str(uuid.uuid4())}


class MockVolume:
    """Mock OpenStack volume"""

    def __init__(self, name: str, size: int = 20, volume_id: str = None):
        self.id = volume_id or str(uuid.uuid4())
        self.name = name
        self.size = size
        self.status = "available"
        self.volume_type = "standard"
        self.attachments = []


class MockConnection:
    """Mock OpenStack connection that simulates SDK responses"""

    def __init__(self):
        # Storage for mock data
        self._projects = {}
        self._users = {}
        self._networks = {}
        self._routers = {}
        self._instances = {}
        self._volumes = {}
        self._flavors = self._create_default_flavors()
        self._images = self._create_default_images()

        # Mock service objects
        self.identity = MockIdentityService(self)
        self.network = MockNetworkService(self)
        self.compute = MockComputeService(self)
        self.block_storage = MockBlockStorageService(self)

    def _create_default_flavors(self) -> Dict[str, MockFlavor]:
        """Create some default flavors"""
        flavors = {
            "m1.tiny": MockFlavor("m1.tiny"),
            "m1.small": MockFlavor("m1.small"),
            "m1.medium": MockFlavor("m1.medium"),
        }
        return flavors

    def _create_default_images(self) -> Dict[str, MockImage]:
        """Create some default images"""
        images = {
            "ubuntu-20.04": MockImage("Ubuntu 20.04 LTS"),
            "ubuntu-22.04": MockImage("Ubuntu 22.04 LTS"),
            "centos-8": MockImage("CentOS 8"),
        }
        return images


class MockRoleAssignment:
    """Mock role assignment object with scope attribute"""

    def __init__(self, project_id, project_name, role_name="member"):
        self.scope = {"project": {"id": project_id, "name": project_name}}
        self.role = {"name": role_name}


class MockIdentityService:
    """Mock OpenStack Identity (Keystone) service"""

    def __init__(self, connection: MockConnection):
        self.conn = connection

    def create_project(self, name: str, description: str = "", **kwargs) -> MockProject:
        """Mock project creation"""
        project = MockProject(name, description)
        self.conn._projects[project.id] = project
        return project

    def find_project(self, name: str) -> Optional[MockProject]:
        """Find project by name"""
        for project in self.conn._projects.values():
            if project.name == name:
                return project
        return None

    def get_project(self, project_id: str) -> Optional[MockProject]:
        """Get project by ID"""
        return self.conn._projects.get(project_id)

    def projects(self) -> List[MockProject]:
        """List all projects"""
        return list(self.conn._projects.values())

    def create_user(
        self, name: str, password: str, email: str = "", **kwargs
    ) -> MockUser:
        """Mock user creation"""
        user = MockUser(name, email)
        self.conn._users[user.id] = user
        return user

    def find_user(self, name: str) -> Optional[MockUser]:
        """Find user by name"""
        for user in self.conn._users.values():
            if user.name == name:
                return user
        # Return a default mock user if not found
        return MockUser(name, f"{name}@test.com")

    def role_assignments(
        self, user_id: str = None, include_names: bool = False
    ) -> List[MockRoleAssignment]:
        """Mock role assignments"""
        # Return mock assignments for testing
        if not self.conn._projects:
            # Create a default project
            default_project = MockProject("default-project", "Default test project")
            self.conn._projects[default_project.id] = default_project

        assignments = []
        for project in self.conn._projects.values():
            assignment = MockRoleAssignment(project.id, project.name, "member")
            assignments.append(assignment)
        return assignments


class MockNetworkService:
    """Mock OpenStack Network (Neutron) service"""

    def __init__(self, connection: MockConnection):
        self.conn = connection

    def create_network(
        self, name: str, project_id: str = None, **kwargs
    ) -> MockNetwork:
        """Mock network creation"""
        network = MockNetwork(name)
        self.conn._networks[network.id] = network
        return network

    def find_network(self, name: str) -> Optional[MockNetwork]:
        """Find network by name"""
        for network in self.conn._networks.values():
            if network.name == name:
                return network
        return None

    def networks(self, **kwargs) -> List[MockNetwork]:
        """List networks"""
        networks = list(self.conn._networks.values())
        # Add some default external networks
        if not networks:
            external_net = MockNetwork("external-network")
            external_net.is_router_external = True
            networks.append(external_net)
        return networks

    def create_subnet(
        self, name: str, network_id: str, cidr: str, **kwargs
    ) -> MockSubnet:
        """Mock subnet creation"""
        subnet = MockSubnet(name, cidr)
        return subnet

    def create_router(self, name: str, **kwargs) -> MockRouter:
        """Mock router creation"""
        router = MockRouter(name)
        self.conn._routers[router.id] = router
        return router

    def get_network(self, network_id: str) -> Optional[MockNetwork]:
        """Get network by ID"""
        return self.conn._networks.get(network_id)

    def create_ip(self, floating_network_id: str) -> Dict:
        """Mock floating IP creation"""
        return {
            "id": str(uuid.uuid4()),
            "floating_ip_address": f"192.168.1.{random.randint(100, 200)}",
            "floating_network_id": floating_network_id,
        }

    def update_ip(self, floating_ip: Dict, port_id: str = None) -> Dict:
        """Mock floating IP update"""
        return floating_ip

    def ports(self, device_id: str = None) -> List[Dict]:
        """Mock network ports"""
        return [{"id": str(uuid.uuid4()), "device_id": device_id}]


class MockComputeService:
    """Mock OpenStack Compute (Nova) service"""

    def __init__(self, connection: MockConnection):
        self.conn = connection

    def find_flavor(self, name: str) -> Optional[MockFlavor]:
        """Find flavor by name"""
        return self.conn._flavors.get(name)

    def find_image(self, name: str) -> Optional[MockImage]:
        """Find image by name"""
        return self.conn._images.get(name)

    def flavors(self) -> List[MockFlavor]:
        """List available flavors"""
        return list(self.conn._flavors.values())

    def images(self) -> List[MockImage]:
        """List available images"""
        return list(self.conn._images.values())

    def create_server(
        self, name: str, image_id: str, flavor_id: str, **kwargs
    ) -> MockInstance:
        """Mock server creation"""
        instance = MockInstance(name)
        self.conn._instances[instance.id] = instance
        return instance

    def wait_for_server(self, server: MockInstance) -> MockInstance:
        """Mock waiting for server to be active"""
        server.status = "ACTIVE"
        return server

    def servers(self) -> List[MockInstance]:
        """List instances"""
        return list(self.conn._instances.values())


class MockBlockStorageService:
    """Mock OpenStack Block Storage (Cinder) service"""

    def __init__(self, connection: MockConnection):
        self.conn = connection

    def create_volume(self, name: str, size: int, **kwargs) -> MockVolume:
        """Mock volume creation"""
        volume = MockVolume(name, size)
        self.conn._volumes[volume.id] = volume
        return volume

    def wait_for_status(
        self, volume: MockVolume, status: str = "available"
    ) -> MockVolume:
        """Mock waiting for volume status"""
        volume.status = status
        return volume

    def volumes(self) -> List[MockVolume]:
        """List volumes"""
        return list(self.conn._volumes.values())


class MockOpenStackUtils:
    """Mock version of OpenStackUtils for testing"""

    @staticmethod
    def get_connection(request=None, project_id=None, system=False):
        """Return mock connection instead of real OpenStack connection"""
        print(
            f"🧪 Mock: Creating connection (system={system}, project_id={project_id})"
        )
        return MockConnection()

    @staticmethod
    def get_openstack_connection(username=None, password=None, project_id=None):
        """Return mock connection instead of real OpenStack connection"""
        print(f"🧪 Mock: Creating connection for user {username}")
        return MockConnection()

    @staticmethod
    def assign_openstack_role(project_name, username, role, conn_token):
        """Mock role assignment - always succeeds"""
        print(f"🧪 Mock: Assigning role {role} to {username} on project {project_name}")
        return True

    @staticmethod
    def get_user_primary_role(openstack_user, project_id, conn_token):
        """Mock user role detection - returns member by default"""
        print(
            f"🧪 Mock: Getting user role for {openstack_user.name if openstack_user else 'unknown'} in project {project_id}"
        )
        return "member"
