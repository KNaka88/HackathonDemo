"""
Security module for Flight Agent
Provides guardrails, monitoring, and security utilities
"""

from .guardrails_config import GuardrailsManager
from .security_monitor import SecurityMonitor, SecurityIncident, monitor_interaction, get_security_status
from .utils import analyze_input_for_threats, sanitize_input, is_legitimate_customer_query
from .config import SUSPICIOUS_PATTERNS, GUARDRAIL_NAMES, SEVERITY_LEVELS, DEFAULT_MODEL_CONFIG

__all__ = [
    'GuardrailsManager',
    'SecurityMonitor', 
    'SecurityIncident',
    'monitor_interaction',
    'get_security_status',
    'analyze_input_for_threats',
    'sanitize_input', 
    'is_legitimate_customer_query',
    'SUSPICIOUS_PATTERNS',
    'GUARDRAIL_NAMES',
    'SEVERITY_LEVELS',
    'DEFAULT_MODEL_CONFIG'
]
