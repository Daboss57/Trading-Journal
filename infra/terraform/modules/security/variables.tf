variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "key_vault_name" {
  type = string
}

variable "key_vault_sku" {
  type    = string
  default = "standard"
}

variable "allowed_ips" {
  type    = list(string)
  default = []
}

variable "log_analytics_workspace_id" {
  type = string
}
