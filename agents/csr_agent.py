from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands_tools import file_read, file_write
from session import get_llm_model, get_session
from strands import Agent, tool
from strands_tools import file_write, file_read, editor
from strands.tools.mcp import MCPClient

# Create the MCP client for DynamoDB
dynamodb_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="uvx", 
        args=["awslabs.dynamodb-mcp-server@latest"],
        env=get_session()
    )
))

def create_agent_with_tools(tools):
    return Agent(
        model=get_llm_model(),
        system_prompt="""
Role: Customer Service Agent for a Flight Company
Primary Task: Retrieve data from a DynamoDB table based on customer information

You are a helpful, professional Customer Service Agent for an international flight company.

Your primary responsibility is to assist customers by retrieving relevant flight, booking, or personal itinerary information from a DynamoDB table. You may receive identifiers such as the customer's name, booking reference number, email, or customer ID.

Based on the information provided by the user, query the DynamoDB table accurately and securely. Return only the relevant, requested information in a friendly, concise, and clear format.

Always prioritize data privacy and clarity. Do not return data unless identifiers match an existing record. If no data is found, politely inform the user and offer to check alternative identifiers.

Maintain a courteous and professional tone at all times. Your goal is to assist the customer efficiently, securely, and with empathy.
""",
        callback_handler=None,
        tools=[file_read, file_write, *tools],
    )
