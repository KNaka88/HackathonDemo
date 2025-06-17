# Multi-Agent Example

This repository contains a multi-agent system built using the Strands Agents framework.

## Project Structure

- `main.py`: Main entry point for the application
- `session.py`: Session management for the agents
- `agents/`: Directory containing agent implementations
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not committed to version control)

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

### 5. Set up environment variables

Copy the example environment file and update it with your settings:

```bash
cp .env.example .env
```

Edit the `.env` file with your AWS credentials and other configuration.

```
AWS_REGION="us-west-2"
AWS_PROFILE="default"
AWS_ACCESS_KEY_ID="ACCESS_KEY"
AWS_SECRET_ACCESS_KEY="SECRET_ACCESS_KEY"
AWS_SESSION_TOKEN="SESSION_TOKEN"
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
