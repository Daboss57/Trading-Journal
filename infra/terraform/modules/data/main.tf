resource "azurerm_postgresql_flexible_server" "this" {
  name                   = var.postgres_name
  resource_group_name    = var.resource_group_name
  location               = var.location
  administrator_login    = var.pg_admin_username
  administrator_password = var.pg_admin_password
  version                = "16"
  sku_name               = var.postgres_sku
  storage_mb             = var.postgres_storage_mb
  zone                   = "1"

  high_availability {
    mode = "ZoneRedundant"
  }

  maintenance_window {
    day_of_week  = 0
    start_hour   = 2
    start_minute = 0
  }

  authentication {
    active_directory_auth_enabled = false
    password_auth_enabled         = true
  }

  backup {
    retention_days   = 7
    geo_redundant_backup = "Enabled"
  }
}

resource "azurerm_redis_cache" "this" {
  name                = var.redis_name
  location            = var.location
  resource_group_name = var.resource_group_name
  capacity            = var.redis_capacity
  family              = var.redis_family
  sku_name            = var.redis_sku
  enable_non_ssl_port = false
}

resource "azurerm_storage_account" "datalake" {
  name                     = var.storage_account_name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  allow_blob_public_access = false
  min_tls_version          = "TLS1_2"
}

output "postgres_fqdn" {
  value = azurerm_postgresql_flexible_server.this.fqdn
}

output "redis_hostname" {
  value = azurerm_redis_cache.this.hostname
}

output "storage_account_id" {
  value = azurerm_storage_account.datalake.id
}
