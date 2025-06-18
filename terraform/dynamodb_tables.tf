# DynamoDB Tables for Flight Agent Application

# Bookings Table
resource "aws_dynamodb_table" "bookings" {
  name         = "Bookings"
  billing_mode = var.billing_mode
  hash_key     = "booking_id"

  attribute {
    name = "booking_id"
    type = "S"
  }

  attribute {
    name = "flight_id"
    type = "S"
  }

  attribute {
    name = "passenger_id"
    type = "S"
  }

  # Provisioned throughput (only used if billing_mode is PROVISIONED)
  read_capacity  = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
  write_capacity = var.billing_mode == "PROVISIONED" ? var.write_capacity : null

  global_secondary_index {
    name            = "FlightIndex"
    hash_key        = "flight_id"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  global_secondary_index {
    name            = "PassengerIndex"
    hash_key        = "passenger_id"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  table_class = var.table_class

  point_in_time_recovery {
    enabled = var.enable_point_in_time_recovery
  }

  server_side_encryption {
    enabled = var.enable_server_side_encryption
  }

  deletion_protection_enabled = var.enable_deletion_protection

  tags = merge(local.common_tags, {
    Name        = "Bookings"
    Description = "Flight booking information and passenger assignments"
    Schema      = "bookings.json"
  })
}

# Passengers Table
resource "aws_dynamodb_table" "passengers" {
  name         = "Passengers"
  billing_mode = var.billing_mode
  hash_key     = "passenger_id"

  attribute {
    name = "passenger_id"
    type = "S"
  }

  attribute {
    name = "frequent_flyer_tier"
    type = "S"
  }

  read_capacity  = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
  write_capacity = var.billing_mode == "PROVISIONED" ? var.write_capacity : null

  global_secondary_index {
    name            = "FrequentFlyerIndex"
    hash_key        = "frequent_flyer_tier"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  table_class = var.table_class

  point_in_time_recovery {
    enabled = var.enable_point_in_time_recovery
  }

  server_side_encryption {
    enabled = var.enable_server_side_encryption
  }

  deletion_protection_enabled = var.enable_deletion_protection

  tags = merge(local.common_tags, {
    Name        = "Passengers"
    Description = "Customer details and frequent flyer data"
    Schema      = "passengers.json"
  })
}

# Flights Table
resource "aws_dynamodb_table" "flights" {
  name         = "Flights"
  billing_mode = var.billing_mode
  hash_key     = "flight_id"

  attribute {
    name = "flight_id"
    type = "S"
  }

  attribute {
    name = "departure_date"
    type = "S"
  }

  attribute {
    name = "origin_airport"
    type = "S"
  }

  read_capacity  = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
  write_capacity = var.billing_mode == "PROVISIONED" ? var.write_capacity : null

  global_secondary_index {
    name            = "DateOriginIndex"
    hash_key        = "departure_date"
    range_key       = "origin_airport"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  table_class = var.table_class

  point_in_time_recovery {
    enabled = var.enable_point_in_time_recovery
  }

  server_side_encryption {
    enabled = var.enable_server_side_encryption
  }

  deletion_protection_enabled = var.enable_deletion_protection

  tags = merge(local.common_tags, {
    Name        = "Flights"
    Description = "Flight schedules and operational data"
    Schema      = "flights.json"
  })
}

# Delays Table
resource "aws_dynamodb_table" "delays" {
  name         = "Delays"
  billing_mode = var.billing_mode
  hash_key     = "delay_id"

  attribute {
    name = "delay_id"
    type = "S"
  }

  attribute {
    name = "flight_id"
    type = "S"
  }

  read_capacity  = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
  write_capacity = var.billing_mode == "PROVISIONED" ? var.write_capacity : null

  global_secondary_index {
    name            = "FlightDelayIndex"
    hash_key        = "flight_id"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  table_class = var.table_class

  point_in_time_recovery {
    enabled = var.enable_point_in_time_recovery
  }

  server_side_encryption {
    enabled = var.enable_server_side_encryption
  }

  deletion_protection_enabled = var.enable_deletion_protection

  tags = merge(local.common_tags, {
    Name        = "Delays"
    Description = "Delay records and impact tracking"
    Schema      = "delays.json"
  })
}

# Rebooking Requests Table
resource "aws_dynamodb_table" "rebooking_requests" {
  name         = "Rebooking_Requests"
  billing_mode = var.billing_mode
  hash_key     = "request_id"

  attribute {
    name = "request_id"
    type = "S"
  }

  attribute {
    name = "passenger_id"
    type = "S"
  }

  attribute {
    name = "original_booking_id"
    type = "S"
  }

  read_capacity  = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
  write_capacity = var.billing_mode == "PROVISIONED" ? var.write_capacity : null

  global_secondary_index {
    name            = "PassengerRequestIndex"
    hash_key        = "passenger_id"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  global_secondary_index {
    name            = "BookingRequestIndex"
    hash_key        = "original_booking_id"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  table_class = var.table_class

  point_in_time_recovery {
    enabled = var.enable_point_in_time_recovery
  }

  server_side_encryption {
    enabled = var.enable_server_side_encryption
  }

  deletion_protection_enabled = var.enable_deletion_protection

  tags = merge(local.common_tags, {
    Name        = "Rebooking_Requests"
    Description = "Rebooking and refund management"
    Schema      = "rebooking_requests.json"
  })
}

# Support Interactions Table
resource "aws_dynamodb_table" "support_interactions" {
  name         = "Support_Interactions"
  billing_mode = var.billing_mode
  hash_key     = "interaction_id"

  attribute {
    name = "interaction_id"
    type = "S"
  }

  attribute {
    name = "passenger_id"
    type = "S"
  }

  attribute {
    name = "interaction_timestamp"
    type = "S"
  }

  read_capacity  = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
  write_capacity = var.billing_mode == "PROVISIONED" ? var.write_capacity : null

  global_secondary_index {
    name            = "PassengerInteractionIndex"
    hash_key        = "passenger_id"
    range_key       = "interaction_timestamp"
    projection_type = "ALL"
    read_capacity   = var.billing_mode == "PROVISIONED" ? var.read_capacity : null
    write_capacity  = var.billing_mode == "PROVISIONED" ? var.write_capacity : null
  }

  table_class = var.table_class

  point_in_time_recovery {
    enabled = var.enable_point_in_time_recovery
  }

  server_side_encryption {
    enabled = var.enable_server_side_encryption
  }

  deletion_protection_enabled = var.enable_deletion_protection

  tags = merge(local.common_tags, {
    Name        = "Support_Interactions"
    Description = "Customer service interaction logs"
    Schema      = "support_interactions.json"
  })
}
