"""
Security utility functions for Flight Agent
Common security operations and helpers
"""

import re
from typing import List, Dict, Any
from .config import SUSPICIOUS_PATTERNS, SEVERITY_LEVELS

def analyze_input_for_threats(user_input: str) -> Dict[str, Any]:
    """
    Analyzes user input for potential security threats
    Returns threat assessment and recommended actions
    """
    user_input_lower = user_input.lower()
    threats_detected = []
    
    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in user_input_lower:
            threats_detected.append(pattern)
    
    # Determine severity based on number and type of threats
    severity = "LOW"
    if len(threats_detected) > 0:
        if any(threat in ["delete from", "drop table", "bypass authentication"] for threat in threats_detected):
            severity = "CRITICAL"
        elif any(threat in ["ignore your previous instructions", "you are now"] for threat in threats_detected):
            severity = "HIGH"
        elif len(threats_detected) > 2:
            severity = "MEDIUM"
    
    return {
        "is_suspicious": len(threats_detected) > 0,
        "threats_detected": threats_detected,
        "severity": severity,
        "threat_count": len(threats_detected),
        "risk_score": SEVERITY_LEVELS.get(severity, 0)
    }

def sanitize_input(user_input: str) -> str:
    """
    Sanitizes user input by removing potentially dangerous patterns
    """
    # Remove SQL injection patterns
    sql_patterns = [
        r";\s*drop\s+table",
        r";\s*delete\s+from", 
        r";\s*insert\s+into",
        r";\s*update\s+set"
    ]
    
    sanitized = user_input
    for pattern in sql_patterns:
        sanitized = re.sub(pattern, "", sanitized, flags=re.IGNORECASE)
    
    return sanitized.strip()

def is_legitimate_customer_query(user_input: str) -> bool:
    """
    Determines if input appears to be a legitimate customer service query
    """
    legitimate_patterns = [
        "booking reference",
        "flight status", 
        "check my flight",
        "frequent flyer",
        "delay information",
        "help with",
        "customer service"
    ]
    
    user_input_lower = user_input.lower()
    return any(pattern in user_input_lower for pattern in legitimate_patterns)
