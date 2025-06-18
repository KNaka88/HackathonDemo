# Flight Agent

**German Airline Customer Support Agent** - An AI-powered customer service system for flight management and passenger assistance using Strands Agents, AWS Bedrock, and Model Context Protocol (MCP).

## Project Overview

This project implements an intelligent customer support agent that helps airline passengers with flight information, booking details, and delay management through a conversational interface. The system demonstrates production-ready integration between modern AI frameworks and cloud services.

## System Architecture

### Core Components

The system follows a layered architecture with clear separation of concerns:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│     UI      │───▶│   Strands   │───▶│   Bedrock   │───▶│     MCP     │
│  (Console)  │    │   Agents    │    │  (Claude)   │    │ (DynamoDB)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Technology Stack

- **UI Layer**: Console interface for user interaction
- **Orchestration**: Strands Agents framework for agent lifecycle management
- **AI Model**: AWS Bedrock with Claude Sonnet 4 (Preview)
- **Data Access**: Model Context Protocol (MCP) for DynamoDB integration
- **Database**: Amazon DynamoDB with comprehensive flight data schemas

## Request Flow & Response Chains

### 1. User Interaction Flow
1. **Input Capture**: Console interface receives passenger query
2. **Agent Invocation**: Strands framework processes the request
3. **AI Analysis**: Bedrock Claude model interprets the query
4. **Tool Selection**: AI determines which MCP tools to use
5. **Data Retrieval**: MCP queries DynamoDB tables
6. **Response Generation**: AI creates natural language response
7. **Output Delivery**: Formatted response displayed to user

### 2. Authentication Flow
- Passenger provides Booking Reference or Frequent Flyer Number
- System validates credentials against passenger database
- Access granted only to authenticated passenger's data
- All interactions logged for security and analytics

### 3. Schema Validation Flow
- **Critical Process**: System reads JSON schema before every database operation
- Data validation prevents database corruption
- Type checking ensures data integrity
- Error handling for invalid operations

### 4. Delay Management Flow
- Real-time flight status monitoring
- Automatic delay detection and notification
- Proactive rebooking assistance
- Cross-referencing between flights, bookings, and passengers

## Key Features

### 🔐 **Security & Authentication**
- Strict passenger authentication requirements
- Data privacy protocols - only authenticated passenger data shown
- Secure database access with read-only permissions
- Comprehensive interaction logging

### 🛫 **Flight Services**
- Real-time flight status and delay information
- Booking retrieval and management
- Automated delay notifications
- Intelligent rebooking assistance

### 🤖 **AI-Powered Support**
- Natural language processing with Claude Sonnet 4
- Professional bilingual support (German/English)
- Intelligent escalation to human agents
- Context-aware conversation management

### 📊 **Schema-First Operations**
- JSON-based schema validation system
- Type safety for all database operations
- Data integrity protection
- Comprehensive error handling

## Data Schema

The system includes comprehensive DynamoDB schemas for:
- **Bookings**: Flight booking information and passenger assignments
- **Passengers**: Customer details and frequent flyer data
- **Flights**: Schedules, status, and operational information
- **Delays**: Delay records and impact tracking
- **Rebooking Requests**: Rebooking and refund management
- **Support Interactions**: Customer service interaction logs

## Project Structure

- `main.py`: Main entry point for the application
- `session.py`: Session management for the agents
- `agents/`: Directory containing agent implementations
  - `csr_agent.py`: Customer Service Representative agent
  - `schema_helper.py`: Schema management and validation helper
- `clients/`: Client-specific configurations and data
- `schemas/`: Schema definitions and validation rules
- `requirements.txt`: Project dependencies
- `pyproject.toml`: Project configuration and dependencies
- `.gitignore`: Git ignore rules

## Prerequisites

- Python 3.13 or higher
- [UV (Astral)](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd hackathon
```

### 2. Set up a virtual environment using UV

```bash
uv venv
```

This will create a virtual environment in the `.venv` directory.

### 3. Activate the virtual environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies using UV

```bash
uv pip install -r requirements.txt
```

Alternatively, you can install from pyproject.toml:

```bash
uv pip install -e .
```

## Running the Application

```bash
python main.py
```

## Development

To add new dependencies:

```bash
uv pip install <package-name>
uv pip freeze > requirements.txt
```

## License

[Specify your license here]
