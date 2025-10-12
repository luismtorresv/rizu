##############################################################################
# Outputs Definition File
# Expose important resource information for reference and automation
##############################################################################

##############################################################################
# Project Outputs
##############################################################################

output "project_id" {
  description = "ID of the created OpenStack project"
  value       = openstack_identity_project_v3.demo.id
}

output "project_name" {
  description = "Name of the created OpenStack project"
  value       = openstack_identity_project_v3.demo.name
}

output "project_enabled" {
  description = "Whether the project is enabled"
  value       = openstack_identity_project_v3.demo.enabled
}

##############################################################################
# Network Outputs
##############################################################################

output "network_id" {
  description = "ID of the private network"
  value       = openstack_networking_network_v2.private.id
}

output "network_name" {
  description = "Name of the private network"
  value       = openstack_networking_network_v2.private.name
}

output "subnet_id" {
  description = "ID of the private subnet"
  value       = openstack_networking_subnet_v2.private.id
}

output "subnet_cidr" {
  description = "CIDR block of the private subnet"
  value       = openstack_networking_subnet_v2.private.cidr
}

output "subnet_gateway_ip" {
  description = "Gateway IP address of the subnet"
  value       = openstack_networking_subnet_v2.private.gateway_ip
}

output "subnet_allocation_pools" {
  description = "IP allocation pools for the subnet"
  value       = openstack_networking_subnet_v2.private.allocation_pool
}

##############################################################################
# Router Outputs
##############################################################################

output "router_id" {
  description = "ID of the router"
  value       = openstack_networking_router_v2.main.id
}

output "router_name" {
  description = "Name of the router"
  value       = openstack_networking_router_v2.main.name
}

output "router_external_network_id" {
  description = "External network ID attached to the router"
  value       = openstack_networking_router_v2.main.external_network_id
}

##############################################################################
# Summary Output
##############################################################################

output "infrastructure_summary" {
  description = "Summary of the created infrastructure"
  value = {
    project = {
      id   = openstack_identity_project_v3.demo.id
      name = openstack_identity_project_v3.demo.name
    }
    network = {
      id   = openstack_networking_network_v2.private.id
      name = openstack_networking_network_v2.private.name
    }
    subnet = {
      id   = openstack_networking_subnet_v2.private.id
      cidr = openstack_networking_subnet_v2.private.cidr
    }
    router = {
      id   = openstack_networking_router_v2.main.id
      name = openstack_networking_router_v2.main.name
    }
  }
}
