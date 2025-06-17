import os
from boto3 import Session
from strands.models import BedrockModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_llm_model():
    """
    Returns a BedrockModel using environment variables for configuration
    """    
    session = Session()    
    return BedrockModel(
        model_id=os.environ.get("BEDROCK_MODEL_ID", "us.anthropic.claude-sonnet-4-20250514-v1:0"),
        boto_session=session,
        temperature=0.01
    )

def get_session():
    session = Session()
    return {
            "AWS_PROFILE": session.profile_name,
            "AWS_REGION": session.region_name,            
            "AWS_ACCESS_KEY_ID": session.get_credentials().access_key,
            "AWS_SECRET_ACCESS_KEY": session.get_credentials().secret_key,
            "AWS_SESSION_TOKEN": session.get_credentials().token
    }