# OpenStack Infrastructure with Terraform

This Terraform configuration creates a complete OpenStack infrastructure including a project, network, subnet, and router.

## 📋 Prerequisites

- Terraform >= 1.0
- Access to an OpenStack environment
- OpenStack credentials with appropriate permissions

## 🏗️ Infrastructure Components

This configuration creates:

- **OpenStack Project (Tenant)**: Isolated project for resource organization
- **Private Network**: Internal network for resources
- **Subnet**: IP address range with DHCP and DNS configuration
- **Router**: Connects the private network to external networks

## 🚀 Quick Start

### 1. Configure Variables

Copy the example variables file and edit with your values:

```bash
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your actual values
```

**⚠️ Security Note**: Never commit `terraform.tfvars` to version control!

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Review the Plan

```bash
terraform plan
```

### 4. Apply the Configuration

```bash
terraform apply
```

### 5. View Outputs

After successful apply, view the created resources:

```bash
terraform output
```

## 🔐 Security Best Practices

### Using Environment Variables (Recommended)

Instead of storing credentials in files, use environment variables:

```bash
export TF_VAR_openstack_user_name="admin"
export TF_VAR_openstack_password="your-secure-password"
export TF_VAR_openstack_auth_url="http://192.168.10.254:5000/v3"

terraform plan
```

### Alternative: OpenStack Clouds Configuration

You can also use OpenStack's `clouds.yaml` configuration:

1. Create `~/.config/openstack/clouds.yaml`:

```yaml
clouds:
  microstack:
    auth:
      auth_url: http://192.168.10.254:5000/v3
      username: admin
      password: your-password
      project_name: admin
      user_domain_name: Default
      project_domain_name: Default
    region_name: microstack
```

2. Update `main.tf` to use the cloud profile:

```hcl
provider "openstack" {
  cloud = "microstack"
}
```

## 📁 File Structure

```
tfs/
├── main.tf                      # Main infrastructure configuration
├── variables.tf                 # Variable definitions
├── outputs.tf                   # Output definitions
├── terraform.tfvars.example     # Example variables file
├── README.md                    # This file
└── .gitignore                   # Git ignore file
```

## 🎛️ Customization

### Changing the Network CIDR

Edit `terraform.tfvars`:

```hcl
subnet_cidr = "10.0.1.0/24"
```

### Connecting to External Network

To enable internet access for instances, set the external network ID:

```hcl
external_network_id = "your-external-network-id"
```

Find available external networks:

```bash
openstack network list --external
```

### Environment Tagging

Set the environment for better resource organization:

```hcl
environment = "production"  # Options: dev, staging, production
```

## 📊 Terraform Commands Reference

| Command | Description |
|---------|-------------|
| `terraform init` | Initialize the working directory |
| `terraform plan` | Preview changes before applying |
| `terraform apply` | Create or update infrastructure |
| `terraform destroy` | Remove all created resources |
| `terraform output` | Display output values |
| `terraform fmt` | Format configuration files |
| `terraform validate` | Validate configuration syntax |
| `terraform state list` | List resources in state |

## 🔄 State Management

### Local State (Default)

By default, Terraform stores state locally in `terraform.tfstate`. 

**⚠️ Important**: Do not commit state files to version control!

### Remote State (Recommended for Teams)

For team collaboration, configure remote state in `main.tf`:

```hcl
terraform {
  backend "s3" {
    bucket = "terraform-state-bucket"
    key    = "openstack/demo/terraform.tfstate"
    region = "us-east-1"
  }
}
```

Or use HTTP backend, Terraform Cloud, or other supported backends.

## 🧹 Cleanup

To destroy all created resources:

```bash
terraform destroy
```

**⚠️ Warning**: This will permanently delete all resources created by this configuration!

## 🐛 Troubleshooting

### Authentication Issues

```bash
# Verify OpenStack credentials
openstack token issue

# Test connectivity
openstack project list
```

### SSL Certificate Errors

For development environments, you can disable SSL verification:

```hcl
openstack_insecure = true
```

**⚠️ Never use in production!**

### State Lock Issues

If state is locked:

```bash
terraform force-unlock <lock-id>
```

## 📚 Additional Resources

- [Terraform OpenStack Provider Documentation](https://registry.terraform.io/providers/terraform-provider-openstack/openstack/latest/docs)
- [OpenStack Documentation](https://docs.openstack.org/)
- [Terraform Best Practices](https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html)

## 📝 License

This configuration is provided as-is for educational and development purposes.
