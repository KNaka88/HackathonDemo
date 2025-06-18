"""
Security configuration constants for Flight Agent
Centralized security settings and patterns
"""

# Security patterns for monitoring
SUSPICIOUS_PATTERNS = [
    # Prompt injection attempts
    "ignore your previous instructions",
    "you are now",
    "forget everything",
    "act as if",
    "pretend to be",
    "override your",
    "system prompt",
    
    # Role manipulation
    "you are not a customer service",
    "become an admin",
    "act as administrator", 
    "change your role",
    
    # Data access attempts
    "show me all",
    "bypass authentication",
    "without booking reference",
    "give me access to",
    "show other passengers",
    
    # Database manipulation
    "delete from",
    "delete all",
    "drop table",
    "insert into",
    "update set",
    "truncate table"
]

# Guardrail configuration
GUARDRAIL_NAMES = [
    "FlightAgentSecurityGuardrails",
    "FlightAgentMinimalGuardrails"
]

# Security severity levels
SEVERITY_LEVELS = {
    "LOW": 1,
    "MEDIUM": 2, 
    "HIGH": 3,
    "CRITICAL": 4
}

# Default model configuration
DEFAULT_MODEL_CONFIG = {
    "model_id": "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "temperature": 0.01
}
