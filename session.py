import os
from boto3 import Session
from strands.models import BedrockModel
from security import GuardrailsManager, DEFAULT_MODEL_CONFIG

def get_llm_model():
    """
    Returns a BedrockModel using environment variables for configuration
    Enhanced with Bedrock Guardrails for security (with fallback)
    """    
    session = Session()
    print(f"🌍 AWS Region: {session.region_name}")
    
    # Try to setup guardrails for security, but continue without them if there are issues
    try:
        guardrails_manager = GuardrailsManager(session)
        guardrails_config = guardrails_manager.setup_guardrails()
        
        print("🔒 Guardrails enabled for enhanced security")
        return BedrockModel(
            model_id=os.environ.get("BEDROCK_MODEL_ID", DEFAULT_MODEL_CONFIG["model_id"]),
            boto_session=session,
            temperature=DEFAULT_MODEL_CONFIG["temperature"],
            guardrail_config={
                "guardrailIdentifier": guardrails_config["guardrail_id"],
                "guardrailVersion": guardrails_config["guardrail_version"]
            }
        )
    except Exception as e:
        print(f"⚠️  Warning: Could not setup Bedrock Guardrails: {str(e)}")
        print("🔄 Continuing with enhanced system prompt security (no guardrails)")
        
        # Fallback to model without guardrails but with enhanced system prompt
        return BedrockModel(
            model_id=os.environ.get("BEDROCK_MODEL_ID", DEFAULT_MODEL_CONFIG["model_id"]),
            boto_session=session,
            temperature=DEFAULT_MODEL_CONFIG["temperature"]
        )

def get_session():
    """
    Returns AWS session configuration as a dictionary
    """
    session = Session()
    return {
        "AWS_PROFILE": session.profile_name,
        "AWS_REGION": session.region_name,            
        "AWS_ACCESS_KEY_ID": session.get_credentials().access_key,
        "AWS_SECRET_ACCESS_KEY": session.get_credentials().secret_key,
        "AWS_SESSION_TOKEN": session.get_credentials().token
    }