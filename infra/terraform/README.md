# Terraform Stack

Modular infrastructure definitions for Azure. Current layout:

```
infra/terraform
├── versions.tf                  # global provider lock
├── modules/
│   ├── network/                 # VNet + subnets
│   ├── data/                    # Postgres Flexible Server, Redis, Blob Storage
│   └── security/                # Key Vault + diagnostics
└── environments/
	└── dev/                     # Example environment wiring modules together
```

## Usage
1. Copy `environments/dev/terraform.tfvars.example` → `terraform.tfvars` and fill in tenant ID + secrets.
2. Initialize from the environment directory:
   ```powershell
   cd infra/terraform/environments/dev
   terraform init
   terraform plan -var-file=terraform.tfvars
   ```
3. Repeat for staging/prod environments as they are added.

## Next Steps
1. Parameterize module outputs for AKS/Container Apps once compute layer is defined.
2. Add Terragrunt wrappers or GitHub Actions workflows for automated plans.
3. Hook diagnostic settings (Log Analytics + alerts) into every resource.
