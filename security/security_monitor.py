"""
Security monitoring utility for Flight Agent
Tracks potential LLM hijacking attempts and security violations
"""

import json
import datetime
from typing import Dict, List, Any
from dataclasses import dataclass, asdict
from .config import SUSPICIOUS_PATTERNS, SEVERITY_LEVELS

@dataclass
class SecurityIncident:
    timestamp: str
    incident_type: str
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL
    description: str
    user_input: str
    agent_response: str
    blocked_by_guardrails: bool = False
    
class SecurityMonitor:
    def __init__(self):
        self.incidents: List[SecurityIncident] = []
        self.suspicious_patterns = SUSPICIOUS_PATTERNS
    
    def analyze_input(self, user_input: str) -> Dict[str, Any]:
        """
        Analyzes user input for potential security threats
        Returns threat assessment and recommended actions
        """
        user_input_lower = user_input.lower()
        threats_detected = []
        severity = "LOW"
        
        # Check for suspicious patterns
        for pattern in self.suspicious_patterns:
            if pattern in user_input_lower:
                threats_detected.append(pattern)
                if pattern in ["ignore your previous instructions", "override your", "system prompt"]:
                    severity = "CRITICAL"
                elif pattern in ["bypass authentication", "show me all", "delete from"]:
                    severity = "HIGH"
                elif pattern in ["you are now", "act as if", "pretend to be"]:
                    severity = "MEDIUM"
        
        # Check for multiple threat indicators
        if len(threats_detected) > 2:
            severity = "HIGH"
        
        return {
            "threats_detected": threats_detected,
            "severity": severity,
            "is_suspicious": len(threats_detected) > 0,
            "risk_score": len(threats_detected) * 10
        }
    
    def log_incident(self, incident_type: str, severity: str, description: str, 
                    user_input: str, agent_response: str, blocked_by_guardrails: bool = False):
        """
        Logs a security incident
        """
        incident = SecurityIncident(
            timestamp=datetime.datetime.now().isoformat(),
            incident_type=incident_type,
            severity=severity,
            description=description,
            user_input=user_input,
            agent_response=agent_response,
            blocked_by_guardrails=blocked_by_guardrails
        )
        
        self.incidents.append(incident)
        
        # Print alert for high severity incidents
        if severity in ["HIGH", "CRITICAL"]:
            print(f"🚨 SECURITY ALERT [{severity}]: {description}")
            print(f"   Time: {incident.timestamp}")
            print(f"   Input: {user_input[:100]}...")
    
    def get_security_report(self) -> Dict[str, Any]:
        """
        Generates a comprehensive security report
        """
        if not self.incidents:
            return {"status": "No security incidents recorded", "incidents": []}
        
        severity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}
        incident_types = {}
        
        for incident in self.incidents:
            severity_counts[incident.severity] += 1
            incident_types[incident.incident_type] = incident_types.get(incident.incident_type, 0) + 1
        
        return {
            "total_incidents": len(self.incidents),
            "severity_breakdown": severity_counts,
            "incident_types": incident_types,
            "recent_incidents": [asdict(incident) for incident in self.incidents[-5:]],
            "guardrails_effectiveness": sum(1 for i in self.incidents if i.blocked_by_guardrails) / len(self.incidents) * 100 if self.incidents else 0
        }
    
    def export_incidents(self, filename: str = "security_incidents.json"):
        """
        Exports all incidents to a JSON file
        """
        with open(filename, 'w') as f:
            json.dump([asdict(incident) for incident in self.incidents], f, indent=2)
        print(f"📄 Security incidents exported to {filename}")

# Global security monitor instance
security_monitor = SecurityMonitor()

def monitor_interaction(user_input: str, agent_response: str) -> Dict[str, Any]:
    """
    Monitors a single interaction for security threats
    """
    analysis = security_monitor.analyze_input(user_input)
    
    if analysis["is_suspicious"]:
        security_monitor.log_incident(
            incident_type="Suspicious Input Pattern",
            severity=analysis["severity"],
            description=f"Detected {len(analysis['threats_detected'])} threat patterns: {', '.join(analysis['threats_detected'])}",
            user_input=user_input,
            agent_response=agent_response
        )
    
    return analysis

def get_security_status() -> Dict[str, Any]:
    """
    Returns current security status and recent incidents
    """
    return security_monitor.get_security_report()
