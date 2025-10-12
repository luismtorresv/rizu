##############################################################################
# Variables Definition File
# Define all input variables for the OpenStack infrastructure
##############################################################################

##############################################################################
# OpenStack Provider Variables
##############################################################################

variable "openstack_user_name" {
  description = "OpenStack username for authentication"
  type        = string
  default     = "admin"
  sensitive   = true
}

variable "openstack_tenant_name" {
  description = "OpenStack tenant/project name for authentication"
  type        = string
  default     = "admin"
}

variable "openstack_password" {
  description = "OpenStack password for authentication"
  type        = string
  sensitive   = true
  # Do not set a default for sensitive values in production
  # Use environment variable TF_VAR_openstack_password instead
}

variable "openstack_auth_url" {
  description = "OpenStack Keystone authentication URL"
  type        = string
  default     = "http://192.168.10.254:5000/v3"
}

variable "openstack_region" {
  description = "OpenStack region name"
  type        = string
  default     = "RegionOne"
}

variable "openstack_domain_name" {
  description = "OpenStack domain name for authentication"
  type        = string
  default     = "Default"
}

variable "openstack_insecure" {
  description = "Allow insecure SSL connections (disable certificate verification)"
  type        = bool
  default     = true
  # Set to false in production with proper SSL certificates
}

##############################################################################
# Project Variables
##############################################################################

variable "project_name" {
  description = "Name of the OpenStack project to create"
  type        = string
  default     = "demo_project"

  validation {
    condition     = length(var.project_name) > 0 && length(var.project_name) <= 64
    error_message = "Project name must be between 1 and 64 characters."
  }
}

variable "project_description" {
  description = "Description of the OpenStack project"
  type        = string
  default     = "Demo project created with Terraform"
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, production)"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

##############################################################################
# Network Variables
##############################################################################

variable "subnet_cidr" {
  description = "CIDR block for the private subnet"
  type        = string
  default     = "192.168.100.0/24"

  validation {
    condition     = can(cidrhost(var.subnet_cidr, 0))
    error_message = "Must be a valid IPv4 CIDR block."
  }
}

variable "dns_nameservers" {
  description = "List of DNS nameservers for the subnet"
  type        = list(string)
  default     = ["8.8.8.8", "8.8.4.4"]
}

variable "external_network_id" {
  description = "ID of the external network for router gateway (optional)"
  type        = string
  default     = null
  # Set this to connect the router to an external network
}
