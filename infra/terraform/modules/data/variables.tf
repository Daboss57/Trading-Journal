variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

variable "postgres_name" {
  type = string
}

variable "postgres_sku" {
  type        = string
  description = "Example: Standard_D2s_v5"
}

variable "postgres_storage_mb" {
  type    = number
  default = 32768
}

variable "pg_admin_username" {
  type = string
}

variable "pg_admin_password" {
  type      = string
  sensitive = true
}

variable "redis_name" {
  type = string
}

variable "redis_capacity" {
  type    = number
  default = 1
}

variable "redis_family" {
  type    = string
  default = "C"
}

variable "redis_sku" {
  type    = string
  default = "Standard"
}

variable "storage_account_name" {
  type = string
}
