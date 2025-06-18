# Outputs for Flight Agent DynamoDB Tables

output "bookings_table_name" {
  description = "Name of the Bookings DynamoDB table"
  value       = aws_dynamodb_table.bookings.name
}

output "bookings_table_arn" {
  description = "ARN of the Bookings DynamoDB table"
  value       = aws_dynamodb_table.bookings.arn
}

output "passengers_table_name" {
  description = "Name of the Passengers DynamoDB table"
  value       = aws_dynamodb_table.passengers.name
}

output "passengers_table_arn" {
  description = "ARN of the Passengers DynamoDB table"
  value       = aws_dynamodb_table.passengers.arn
}

output "flights_table_name" {
  description = "Name of the Flights DynamoDB table"
  value       = aws_dynamodb_table.flights.name
}

output "flights_table_arn" {
  description = "ARN of the Flights DynamoDB table"
  value       = aws_dynamodb_table.flights.arn
}

output "delays_table_name" {
  description = "Name of the Delays DynamoDB table"
  value       = aws_dynamodb_table.delays.name
}

output "delays_table_arn" {
  description = "ARN of the Delays DynamoDB table"
  value       = aws_dynamodb_table.delays.arn
}

output "rebooking_requests_table_name" {
  description = "Name of the Rebooking Requests DynamoDB table"
  value       = aws_dynamodb_table.rebooking_requests.name
}

output "rebooking_requests_table_arn" {
  description = "ARN of the Rebooking Requests DynamoDB table"
  value       = aws_dynamodb_table.rebooking_requests.arn
}

output "support_interactions_table_name" {
  description = "Name of the Support Interactions DynamoDB table"
  value       = aws_dynamodb_table.support_interactions.name
}

output "support_interactions_table_arn" {
  description = "ARN of the Support Interactions DynamoDB table"
  value       = aws_dynamodb_table.support_interactions.arn
}

# Summary output for all table names
output "all_table_names" {
  description = "List of all DynamoDB table names"
  value = [
    aws_dynamodb_table.bookings.name,
    aws_dynamodb_table.passengers.name,
    aws_dynamodb_table.flights.name,
    aws_dynamodb_table.delays.name,
    aws_dynamodb_table.rebooking_requests.name,
    aws_dynamodb_table.support_interactions.name
  ]
}

# Summary output for all table ARNs
output "all_table_arns" {
  description = "List of all DynamoDB table ARNs"
  value = [
    aws_dynamodb_table.bookings.arn,
    aws_dynamodb_table.passengers.arn,
    aws_dynamodb_table.flights.arn,
    aws_dynamodb_table.delays.arn,
    aws_dynamodb_table.rebooking_requests.arn,
    aws_dynamodb_table.support_interactions.arn
  ]
}
