# Flight Agent DynamoDB Infrastructure

This Terraform configuration creates the DynamoDB tables required for the German Airline Customer Support Agent application.

## Architecture Overview

The infrastructure includes 6 DynamoDB tables that support the flight management and customer service operations:

1. **Bookings** - Flight booking information and passenger assignments
2. **Passengers** - Customer details and frequent flyer data  
3. **Flights** - Flight schedules, status, and operational information
4. **Delays** - Delay records and impact tracking
5. **Rebooking_Requests** - Rebooking and refund management
6. **Support_Interactions** - Customer service interaction logs

## Table Relationships

```
Passengers ──┐
             ├── Bookings ──── Flights ──── Delays
             └── Rebooking_Requests
             └── Support_Interactions
```

## Features

- **Pay-per-request billing** by default (configurable to provisioned)
- **Global Secondary Indexes** for efficient querying
- **Point-in-time recovery** enabled for data protection
- **Server-side encryption** for data security
- **Comprehensive tagging** for resource management
- **Configurable deletion protection** for production environments

## Prerequisites

- Terraform >= 1.0
- AWS CLI configured with appropriate permissions
- AWS provider ~> 5.0

## Required AWS Permissions

Your AWS credentials need the following DynamoDB permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:CreateTable",
                "dynamodb:DescribeTable",
                "dynamodb:UpdateTable",
                "dynamodb:DeleteTable",
                "dynamodb:TagResource",
                "dynamodb:UntagResource",
                "dynamodb:ListTagsOfResource"
            ],
            "Resource": "*"
        }
    ]
}
```

## Quick Start

1. **Clone and navigate to the terraform directory:**
   ```bash
   cd terraform
   ```

2. **Copy the example variables file:**
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   ```

3. **Edit terraform.tfvars with your configuration:**
   ```bash
   # Example configuration
   aws_region = "us-west-2"
   environment = "dev"
   project_name = "flight-agent"
   ```

4. **Initialize Terraform:**
   ```bash
   terraform init
   ```

5. **Plan the deployment:**
   ```bash
   terraform plan
   ```

6. **Apply the configuration:**
   ```bash
   terraform apply
   ```

## Configuration Options

### Basic Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `aws_region` | AWS region for DynamoDB tables | `us-west-2` | No |
| `environment` | Environment name (dev/staging/prod) | `dev` | No |
| `project_name` | Project name for resource naming | `flight-agent` | No |

### DynamoDB Configuration

| Variable | Description | Default | Options |
|----------|-------------|---------|---------|
| `billing_mode` | DynamoDB billing mode | `PAY_PER_REQUEST` | `PAY_PER_REQUEST`, `PROVISIONED` |
| `table_class` | DynamoDB table class | `STANDARD` | `STANDARD`, `STANDARD_INFREQUENT_ACCESS` |
| `enable_point_in_time_recovery` | Enable PITR | `true` | `true`, `false` |
| `enable_server_side_encryption` | Enable SSE | `true` | `true`, `false` |
| `enable_deletion_protection` | Enable deletion protection | `false` | `true`, `false` |

### Provisioned Throughput (when billing_mode = "PROVISIONED")

| Variable | Description | Default | Range |
|----------|-------------|---------|-------|
| `read_capacity` | Read capacity units | `5` | 1-40000 |
| `write_capacity` | Write capacity units | `5` | 1-40000 |

## Environment-Specific Configurations

### Development
```hcl
environment = "dev"
billing_mode = "PAY_PER_REQUEST"
enable_deletion_protection = false
```

### Production
```hcl
environment = "prod"
billing_mode = "PAY_PER_REQUEST"  # or "PROVISIONED" for predictable workloads
enable_deletion_protection = true
enable_point_in_time_recovery = true
```

## Table Schemas

Each table follows the schema definitions in the `../schemas/` directory:

- `bookings.json` - Bookings table schema
- `passengers.json` - Passengers table schema  
- `flights.json` - Flights table schema
- `delays.json` - Delays table schema
- `rebooking_requests.json` - Rebooking requests schema
- `support_interactions.json` - Support interactions schema

## Global Secondary Indexes

### Bookings Table
- **FlightIndex**: Query bookings by flight_id
- **PassengerIndex**: Query bookings by passenger_id

### Passengers Table  
- **FrequentFlyerIndex**: Query passengers by frequent_flyer_tier

### Flights Table
- **DateOriginIndex**: Query flights by departure_date and origin_airport

### Delays Table
- **FlightDelayIndex**: Query delays by flight_id

### Rebooking_Requests Table
- **PassengerRequestIndex**: Query requests by passenger_id
- **BookingRequestIndex**: Query requests by original_booking_id

### Support_Interactions Table
- **PassengerInteractionIndex**: Query interactions by passenger_id and timestamp

## Outputs

After successful deployment, Terraform provides:

- Individual table names and ARNs
- Complete list of all table names
- Complete list of all table ARNs

## Cost Optimization

### Pay-per-Request (Recommended)
- No upfront costs
- Automatic scaling
- Pay only for actual usage
- Ideal for variable workloads

### Provisioned Throughput
- Predictable costs
- Reserved capacity
- Better for consistent workloads
- Requires capacity planning

## Monitoring and Maintenance

### CloudWatch Metrics
All tables automatically publish metrics to CloudWatch:
- Read/Write capacity utilization
- Throttled requests
- System errors
- User errors

### Point-in-Time Recovery
- Enabled by default
- 35-day retention period
- Continuous backups
- Restore to any point in time

## Security Features

- **Server-side encryption** using AWS managed keys
- **IAM-based access control** 
- **VPC endpoints** support (configure separately)
- **Resource-based policies** support

## Troubleshooting

### Common Issues

1. **Insufficient Permissions**
   ```
   Error: AccessDeniedException
   ```
   Solution: Ensure your AWS credentials have the required DynamoDB permissions.

2. **Table Already Exists**
   ```
   Error: ResourceInUseException
   ```
   Solution: Import existing tables or use different table names.

3. **Invalid Configuration**
   ```
   Error: ValidationException
   ```
   Solution: Check variable values against validation rules.

### Validation Commands

```bash
# Validate Terraform configuration
terraform validate

# Check formatting
terraform fmt -check

# Plan with detailed output
terraform plan -detailed-exitcode
```

## Cleanup

To destroy all resources:

```bash
terraform destroy
```

**Warning**: This will permanently delete all tables and data. Ensure you have backups if needed.

## Integration with Application

The application uses the AWS DynamoDB MCP server to interact with these tables:

```python
# Example from clients/dynamodb_client.py
dynamodb_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="uvx", 
        args=["awslabs.dynamodb-mcp-server@latest"],
        env=get_session()
    )
))
```

## Support

For issues related to:
- **Terraform configuration**: Check this README and Terraform documentation
- **DynamoDB**: Refer to AWS DynamoDB documentation
- **Application integration**: See the main project README

## Contributing

When modifying the infrastructure:

1. Update schema files in `../schemas/` first
2. Modify Terraform configuration accordingly
3. Test in development environment
4. Update this README if needed
5. Plan and apply changes carefully in production
