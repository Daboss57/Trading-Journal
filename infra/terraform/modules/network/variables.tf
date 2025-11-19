variable "resource_group_name" {
  type = string
}

variable "vnet_name" {
  type = string
}

variable "location" {
  type = string
}

variable "address_space" {
  type = list(string)
}

variable "app_subnet_prefix" {
  type = string
}

variable "data_subnet_prefix" {
  type = string
}
