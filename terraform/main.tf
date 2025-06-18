# Flight Agent DynamoDB Tables
# Terraform configuration for German Airline Customer Support Agent

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Local values for common tags and configuration
locals {
  common_tags = merge({
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "Terraform"
    Application = "German-Airline-Customer-Support"
  }, var.additional_tags)

  # Common table configuration
  table_config = {
    billing_mode           = var.billing_mode
    table_class            = var.table_class
    point_in_time_recovery = var.enable_point_in_time_recovery
    server_side_encryption = var.enable_server_side_encryption
    deletion_protection    = var.enable_deletion_protection
  }
}

# DynamoDB tables are defined in dynamodb_tables.tf
