import ipaddress
import secrets
import string
from Rizu.Openstack.Utils import OpenStackUtils
from openstack import exceptions


class OpenStackBuilders:

    @staticmethod
    def create_openstack_project(
        conn_token, project_name, project_description, user, role
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
    def create_openstack_user(
        conn_token,
        user,
    ):
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
    def create_openstack_network(
        conn_token,
        network_name,
        project_id,
        cidr=None,
        gateway_ip=None,
        is_external=False,
    ):
        try:
            # Connect directly with project scope
            network = conn_token.network.create_network(
                name=network_name,
                project_id=project_id,
                is_router_external=is_external,
                admin_state_up=True,
            )

            # Assign a default CIDR if none provided
            if not cidr:
                # Pick a default subnet pool, e.g., 10.0.X.0/24
                # Here we use 10.0.0.0/24 for simplicity
                cidr = "10.0.0.0/24"

            # Validate CIDR format
            try:
                subnet_network = ipaddress.IPv4Network(cidr)
            except ValueError:
                raise ValueError(f"Invalid CIDR format: {cidr}")

            # Assign default gateway if not provided
            if not gateway_ip:
                gateway_ip = str(subnet_network[1])  # first usable IP

            # Optional: check for overlapping subnets in the project
            existing_subnets = list(conn_token.network.subnets(project_id=project_id))
            for s in existing_subnets:
                existing_cidr = ipaddress.IPv4Network(s.cidr)
                if subnet_network.overlaps(existing_cidr):
                    raise ValueError(
                        f"CIDR {cidr} overlaps with existing subnet {s.name} ({s.cidr})"
                    )
            # Create the subnet
            _ = conn_token.network.create_subnet(
                name=f"{network_name}-subnet",
                network_id=network.id,
                ip_version=4,
                cidr=cidr,
                gateway_ip=gateway_ip,
                enable_dhcp=not is_external,
                project_id=project_id,
            )

            return network

        except (exceptions.HttpException, ValueError) as e:
            print(f"Failed to create network {network_name}: {e}")
            return None

    @staticmethod
    def create_openstack_router(
        conn_token, router_name, project_id, external_network_name=None
    ):
        try:
            # Find internal network for the project
            internal_net = next(
                (
                    n
                    for n in conn_token.network.networks(project_id=project_id)
                    if not n.is_router_external
                ),
                None,
            )
            if not internal_net:
                raise ValueError(f"No internal network found for project {project_id}")

            # Pick its first subnet
            subnet = next(conn_token.network.subnets(network_id=internal_net.id), None)
            if not subnet:
                raise ValueError(f"No subnet found for network {internal_net.name}")

            # Prepare router kwargs
            kwargs = {
                "name": router_name,
                "project_id": project_id,
                "admin_state_up": True,
            }

            if external_network_name:
                ext_net = conn_token.network.find_network(
                    external_network_name,
                    external=True,
                )
                if not ext_net:
                    raise ValueError(
                        f"External network {external_network_name} not found"
                    )
                kwargs["external_gateway_info"] = {
                    "network_id": ext_net.id,
                    "enable_snat": True,
                }

            # Create router
            router = conn_token.network.create_router(**kwargs)
            print(f"Created router {router.name}")

            # Attach internal subnet
            conn_token.network.add_interface_to_router(router, subnet_id=subnet.id)
            print(f"Attached subnet {subnet.name} to router {router.name}")

            # Refresh router to verify external link
            router = conn_token.network.get_router(router.id)
            if router.external_gateway_info:
                print(f"Connected to external network: {external_network_name}")
            else:
                print("⚠️ External gateway not set.")

            return router

        except Exception as e:
            print(f"Failed to create router {router_name}: {e}")
            return None

    def create_openstack_vm(
        conn_token,
        flavor_name,
        image_name,
        private_network_name,
        external_network_id,
        vm_name,
    ):
        try:
            # Find the resources
            flavor = conn_token.compute.find_flavor(flavor_name)
            image = conn_token.compute.find_image(image_name)
            network = conn_token.network.find_network(private_network_name)

            if not (flavor and image and network):
                raise ValueError("One or more resources not found.")

            # Create the VM
            vm = conn_token.compute.create_server(
                name=vm_name,
                image_id=image.id,
                flavor_id=flavor.id,
                networks=[{"uuid": network.id}],
            )

            # Wait for it to become ACTIVE
            vm = conn_token.compute.wait_for_server(vm)

            # Find external net
            ext_net = conn_token.network.get_network(external_network_id)
            if not ext_net:
                raise ValueError(f"External network '{external_network_id}' not found")

            # Create floating IP and assign it to a port
            floating_ip = conn_token.network.create_ip(floating_network_id=ext_net.id)

            ports = list(conn_token.network.ports(device_id=vm.id))
            if not ports:
                raise ValueError(f"No network ports found for VM {vm_name}")

            conn_token.network.update_ip(floating_ip, port_id=ports[0].id)
            print(
                f"Associated floating IP {floating_ip.floating_ip_address} to VM {vm_name}"
            )

            return vm

        except Exception as e:
            print(f"Failed to create VM {vm_name}: {e}")
            return None
