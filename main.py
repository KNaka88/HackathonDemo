#!/usr/bin/env python3
from agents.csr_agent import create_agent_with_tools, dynamodb_client

import logging

logging.getLogger("strands").setLevel(logging.ERROR)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    print("\n📁 Flight Assist Agent 📁\n")
    print("Type 'exit' to quit.")

    # Interactive loop
    with dynamodb_client:
        # Get MCP tools and create agent
        mcp_tools = dynamodb_client.list_tools_sync()
        agent = create_agent_with_tools(mcp_tools)
        
        while True:
            try:
                user_input = input("\n> ")
                if user_input.lower() == "exit":
                    print("\nGoodbye! 👋")
                    break

                response = agent(
                    user_input, 
                )
                
                # Extract and print only the relevant content from the specialized agent's response
                content = str(response)
                print(content)
                
            except KeyboardInterrupt:
                print("\n\nExecution interrupted. Exiting...")
                break
            except Exception as e:
                print(f"\nAn error occurred: {str(e)}")
                print("Please try asking a different question.")