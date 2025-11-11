"""
Mock OpenStack Builders for Testing

This module provides mock implementations of OpenStack builders that simulate
OpenStack operations without requiring actual connections.
"""

from .MockUtils import (
    MockConnection,
    MockProject,
    MockNetwork,
    MockRouter,
    MockInstance,
    MockVolume,
)
import time
import random


class MockOpenStackBuilders:
    """Mock version of OpenStackBuilders for testing"""

    @staticmethod
    def create_openstack_project(
        conn_token, project_name, project_description, user, role
    ):
        """Mock project creation - always succeeds"""
        try:
            # Simulate project creation delay
            time.sleep(0.1)

            # Create mock project
            project = conn_token.identity.create_project(
                name=project_name, description=project_description
            )

            # Mock role assignment
            print(
                f"Mock: Created project {project_name} and assigned role {role} to {user.username}"
            )
            return True

        except Exception as e:
            print(f"Mock: Project creation failed: {e}")
            return False

    @staticmethod
    def generate_password(length=16):
        """Generate a mock password"""
        return "mock_password_123!"

    @staticmethod
    def create_openstack_user(conn_token, user):
        """Mock user creation - always succeeds"""
        try:
            # Generate mock password
            mock_password = MockOpenStackBuilders.generate_password()

            # Create mock user
            openstack_user = conn_token.identity.create_user(
                name=user.username, password=mock_password, email=user.email
            )

            # Set mock password (in real app this would be saved)
            user.openstack_password = mock_password
            print(f"Mock: Created OpenStack user {user.username}")
            return True

        except Exception as e:
            print(f"Mock: User creation failed: {e}")
            return False

    @staticmethod
    def create_openstack_network(
        conn_token,
        network_name,
        project_id,
        cidr=None,
        gateway_ip=None,
        is_external=False,
    ):
        """Mock network creation"""
        try:
            # Set defaults
            if not cidr:
                cidr = "10.0.0.0/24"
            if not gateway_ip:
                gateway_ip = "10.0.0.1"

            # Create mock network
            network = conn_token.network.create_network(
                name=network_name, project_id=project_id, is_router_external=is_external
            )

            # Create mock subnet
            subnet = conn_token.network.create_subnet(
                name=f"{network_name}-subnet",
                network_id=network.id,
                cidr=cidr,
                gateway_ip=gateway_ip,
            )

            print(f"Mock: Created network {network_name} with subnet {cidr}")
            return network

        except Exception as e:
            print(f"Mock: Network creation failed: {e}")
            return None

    @staticmethod
    def create_openstack_router(
        conn_token, router_name, project_id, external_network_name=None
    ):
        """Mock router creation"""
        try:
            # Create mock router
            router = conn_token.network.create_router(
                name=router_name, project_id=project_id
            )

            # Mock external gateway attachment
            if external_network_name:
                print(
                    f"Mock: Attached router {router_name} to external network {external_network_name}"
                )

            print(f"Mock: Created router {router_name}")
            return router

        except Exception as e:
            print(f"Mock: Router creation failed: {e}")
            return None

    @staticmethod
    def create_openstack_vm(
        conn_token,
        flavor_name,
        image_name,
        private_network_name,
        external_network_id,
        vm_name,
    ):
        """Mock VM creation"""
        try:
            # Find mock resources
            flavor = conn_token.compute.find_flavor(flavor_name)
            image = conn_token.compute.find_image(image_name)
            network = conn_token.network.find_network(private_network_name)

            if not flavor:
                # Create a default flavor if not found
                flavor = conn_token.compute._conn._flavors.get("m1.small")

            if not image:
                # Create a default image if not found
                image = conn_token.compute._conn._images.get("ubuntu-20.04")

            # Create mock VM
            vm = conn_token.compute.create_server(
                name=vm_name,
                image_id=image.id if image else "mock-image-id",
                flavor_id=flavor.id if flavor else "mock-flavor-id",
                networks=[{"uuid": network.id if network else "mock-network-id"}],
            )

            # Mock wait for active
            vm = conn_token.compute.wait_for_server(vm)

            # Mock floating IP assignment
            floating_ip = conn_token.network.create_ip(
                floating_network_id=external_network_id
            )

            # Mock port attachment
            ports = conn_token.network.ports(device_id=vm.id)
            if ports:
                conn_token.network.update_ip(floating_ip, port_id=ports[0]["id"])

            print(
                f"Mock: Created VM {vm_name} with IP {floating_ip['floating_ip_address']}"
            )
            return vm

        except Exception as e:
            print(f"Mock: VM creation failed: {e}")
            return None

    @staticmethod
    def create_openstack_volume(
        conn_token, volume_name, size_gb, vm_id=None, description=None
    ):
        """Mock volume creation"""
        try:
            # Create mock volume
            volume = conn_token.block_storage.create_volume(
                name=volume_name, size=size_gb, description=description
            )

            # Mock wait for available status
            volume = conn_token.block_storage.wait_for_status(volume, "available")

            # Mock attachment to VM if specified
            if vm_id:
                # Simulate attachment delay
                time.sleep(0.2)
                volume.attachments.append(
                    {
                        "server_id": vm_id,
                        "device": f"/dev/vd{chr(98 + len(volume.attachments))}",  # /dev/vdb, /dev/vdc, etc.
                    }
                )
                volume.status = "in-use"
                print(f"Mock: Attached volume {volume_name} to VM {vm_id}")

            print(f"Mock: Created volume {volume_name} ({size_gb}GB)")
            return volume

        except Exception as e:
            print(f"Mock: Volume creation failed: {e}")
            return None
