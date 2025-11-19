variable "location" {
  type    = string
  default = "eastus"
}

variable "pg_admin_username" {
  type = string
}

variable "pg_admin_password" {
  type      = string
  sensitive = true
}

variable "storage_account_name" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "key_vault_allowed_ips" {
  type    = list(string)
  default = []
}

variable "log_analytics_workspace_id" {
  type = string
}
