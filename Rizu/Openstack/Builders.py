import ipaddress
import secrets
import string
from Rizu.Openstack.Utils import OpenStackUtils
from openstack import exceptions


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
    def create_openstack_network(
        network_name,
        project_id,
        conn_token,
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
