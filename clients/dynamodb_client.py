from mcp import StdioServerParameters, stdio_client
from session import get_session
from strands.tools.mcp import MCPClient

# Create the MCP client for DynamoDB
dynamodb_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="uvx", 
        args=["awslabs.dynamodb-mcp-server@latest"],
        env=get_session()
    )
))