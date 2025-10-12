##############################################################################
# Terraform Configuration for OpenStack Infrastructure
# This configuration creates a complete network infrastructure including:
# - Project (tenant)
# - Private network and subnet
# - Router with subnet attachment
##############################################################################
terraform {
required_version = ">= 1.0"
required_providers {
openstack = {
source  = "terraform-provider-openstack/openstack"
version = "~> 1.54.1"
}
}
# Optional: Configure remote backend for state management
# Uncomment and configure for production use
# backend "s3" {
#   bucket = "terraform-state-bucket"
#   key    = "openstack/demo/terraform.tfstate"
#   region = "us-east-1"
# }
}
##############################################################################
# Provider Configuration
# Note: For production, use environment variables or a credentials file
# instead of hardcoding sensitive values
##############################################################################
provider "openstack" {
user_name   = var.openstack_user_name
tenant_name = var.openstack_tenant_name
password    = var.openstack_password
auth_url    = var.openstack_auth_url
region      = var.openstack_region
domain_name = var.openstack_domain_name
insecure    = var.openstack_insecure
}
##############################################################################
# Project (Tenant) Resources
##############################################################################
# Create a new OpenStack project for resource isolation
resource "openstack_identity_project_v3" "demo" {
name        = var.project_name
description = var.project_description
domain_id   = "default"
enabled     = true
tags = [
"terraform-managed",
"environment:${var.environment}",
]
}
##############################################################################
# Networking Resources
##############################################################################
# Create a private network within the project
resource "openstack_networking_network_v2" "private" {
name           = "${var.project_name}-network"
description    = "Private network for ${var.project_name}"
admin_state_up = true
tenant_id      = openstack_identity_project_v3.demo.id
tags = [
"terraform-managed",
"project:${var.project_name}",
]
}
# Create a subnet within the private network
resource "openstack_networking_subnet_v2" "private" {
name            = "${var.project_name}-subnet"
description     = "Private subnet for ${var.project_name}"
network_id      = openstack_networking_network_v2.private.id
cidr            = var.subnet_cidr
ip_version      = 4
dns_nameservers = var.dns_nameservers
tenant_id       = openstack_identity_project_v3.demo.id
# Allocation pool to reserve IPs for specific uses
allocation_pool {
start = cidrhost(var.subnet_cidr, 10)
end   = cidrhost(var.subnet_cidr, 250)
}
tags = [
"terraform-managed",
"project:${var.project_name}",
]
}
# Create a router for connecting the private network to external networks
resource "openstack_networking_router_v2" "main" {
name                = "${var.project_name}-router"
description         = "Main router for ${var.project_name}"
admin_state_up      = true
tenant_id           = openstack_identity_project_v3.demo.id
external_network_id = var.external_network_id
tags = [
"terraform-managed",
"project:${var.project_name}",
]
}
# Attach the subnet to the router for routing capabilities
resource "openstack_networking_router_interface_v2" "main" {
router_id = openstack_networking_router_v2.main.id
subnet_id = openstack_networking_subnet_v2.private.id
}