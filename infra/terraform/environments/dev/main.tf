terraform {
  backend "local" {}
}

provider "azurerm" {
  features {}
}

locals {
  prefix = "tj-dev"
}

resource "azurerm_resource_group" "this" {
  name     = "${local.prefix}-rg"
  location = var.location
}

module "network" {
  source              = "../../modules/network"
  resource_group_name = azurerm_resource_group.this.name
  vnet_name           = "${local.prefix}-vnet"
  location            = var.location
  address_space       = ["10.10.0.0/16"]
  app_subnet_prefix   = "10.10.1.0/24"
  data_subnet_prefix  = "10.10.2.0/24"
}

module "data" {
  source               = "../../modules/data"
  resource_group_name  = azurerm_resource_group.this.name
  location             = var.location
  postgres_name        = "${local.prefix}-pg"
  postgres_sku         = "Standard_D4s_v5"
  pg_admin_username    = var.pg_admin_username
  pg_admin_password    = var.pg_admin_password
  postgres_storage_mb  = 65536
  redis_name           = "${local.prefix}-redis"
  redis_capacity       = 1
  redis_family         = "C"
  redis_sku            = "Standard"
  storage_account_name = var.storage_account_name
}

module "security" {
  source                       = "../../modules/security"
  resource_group_name          = azurerm_resource_group.this.name
  location                     = var.location
  tenant_id                    = var.tenant_id
  key_vault_name               = "${local.prefix}-kv"
  key_vault_sku                = "standard"
  allowed_ips                  = var.key_vault_allowed_ips
  log_analytics_workspace_id   = var.log_analytics_workspace_id
}
