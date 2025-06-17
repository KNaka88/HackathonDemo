#!/usr/bin/env python3
from agents.csr_agent import create_csr_agent
from clients.dynamodb_client import dynamodb_client

import logging

logging.getLogger("strands").setLevel(logging.ERROR)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    print("\n📁 Flight Assist Agent 📁\n")
    print("Type 'exit' to quit.\n")
    print("Guten Tag! Welcome to German Airline Customer Support. I'm here to help you with your flight information and booking inquiries.\n")
    print("To ensure I can provide you with accurate and secure access to your flight details, I'll need to verify your identity first. Please provide either:\n")
    print("• Your Frequent Flyer Number, or")
    print("• Your Booking ID/Reference Number\n")
    print("Once I have this information, I'll be able to assist you with your flight status, check for any delays, and help with any questions you may have about your booking.\n")

    with dynamodb_client:
        # Get MCP tools and create agent
        mcp_tools = dynamodb_client.list_tools_sync()
        csr_agent = create_csr_agent(mcp_tools)
        
        while True:
            try:
                user_input = input("\n> ")
                if user_input.lower() == "exit":
                    print("\nGoodbye! 👋")
                    break

                response = csr_agent(
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