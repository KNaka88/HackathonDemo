"""
Schema Helper Functions for Database Operations
"""
from strands import tool
import json
import os

@tool
def read_table_schema(table_name: str) -> str:
    """
    Read and return the schema for a specific DynamoDB table.
    
    Args:
        table_name: Name of the table (e.g., 'Bookings', 'Passengers', 'Support_Interactions')
    
    Returns:
        str: JSON schema content for the specified table
    """
    # Map table names to schema files
    schema_mapping = {
        'Bookings': 'bookings.json',
        'Passengers': 'passengers.json', 
        'Flights': 'flights.json',
        'Delays': 'delays.json',
        'Rebooking_Requests': 'rebooking_requests.json',
        'Support_Interactions': 'support_interactions.json'
    }
    
    if table_name not in schema_mapping:
        return f"Error: Unknown table name '{table_name}'. Available tables: {list(schema_mapping.keys())}"
    
    schema_file = schema_mapping[table_name]
    schema_path = f"./schemas/{schema_file}"
    
    try:
        if os.path.exists(schema_path):
            with open(schema_path, 'r') as f:
                schema_content = f.read()
            return f"Schema for {table_name} table:\n{schema_content}"
        else:
            return f"Error: Schema file not found at {schema_path}"
    except Exception as e:
        return f"Error reading schema file: {str(e)}"

@tool
def validate_update_data(table_name: str, update_data: dict) -> str:
    """
    Validate update data against table schema before performing database operations.
    
    Args:
        table_name: Name of the table to validate against
        update_data: Dictionary containing the data to be updated
    
    Returns:
        str: Validation result with any issues found
    """
    # First read the schema
    schema_result = read_table_schema(table_name)
    
    if schema_result.startswith("Error:"):
        return schema_result
    
    try:
        # Extract JSON from schema result
        schema_json_start = schema_result.find('{')
        if schema_json_start == -1:
            return "Error: Could not parse schema JSON"
        
        schema_json = schema_result[schema_json_start:]
        schema = json.loads(schema_json)
        
        # Validate each field in update_data
        validation_issues = []
        schema_attributes = schema.get('attributes', {})
        
        for field_name, field_value in update_data.items():
            if field_name not in schema_attributes:
                validation_issues.append(f"Field '{field_name}' not found in schema")
                continue
            
            field_schema = schema_attributes[field_name]
            expected_type = field_schema.get('type')
            
            # Basic type validation
            if expected_type == 'String' and not isinstance(field_value, str):
                validation_issues.append(f"Field '{field_name}' should be String, got {type(field_value).__name__}")
            elif expected_type == 'Number' and not isinstance(field_value, (int, float)):
                validation_issues.append(f"Field '{field_name}' should be Number, got {type(field_value).__name__}")
            elif expected_type == 'Boolean' and not isinstance(field_value, bool):
                validation_issues.append(f"Field '{field_name}' should be Boolean, got {type(field_value).__name__}")
        
        if validation_issues:
            return f"Validation issues found:\n" + "\n".join(validation_issues)
        else:
            return f"Validation successful: All fields in update_data are valid for {table_name} table"
    
    except json.JSONDecodeError as e:
        return f"Error parsing schema JSON: {str(e)}"
    except Exception as e:
        return f"Error during validation: {str(e)}"
