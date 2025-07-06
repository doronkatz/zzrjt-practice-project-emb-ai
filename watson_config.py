"""
Configuration for Watson Sentiment Analysis API endpoints
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Choose which endpoint to use
USE_PUBLIC_WATSON = os.environ.get('USE_PUBLIC_WATSON', 'false').lower() == 'true'

# Coursera internal endpoint (only works within Coursera network)
COURSERA_ENDPOINT = {
    "url": "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict",
    "headers": {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    },
    "payload_format": lambda text: {
        "raw_document": {
            "text": text
        }
    }
}

# IBM Watson Natural Language Understanding public API
# To use this:
# 1. Create an IBM Cloud account at https://cloud.ibm.com
# 2. Create a Watson Natural Language Understanding service instance
# 3. Get your API key and URL from the service credentials
# 4. Set environment variables: WATSON_API_KEY and WATSON_URL
PUBLIC_WATSON_ENDPOINT = {
    "url": os.environ.get('WATSON_URL', 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze?version=2022-04-07'),
    "headers": {
        "Content-Type": "application/json"
    },
    "payload_format": lambda text: {
        "text": text,
        "features": {
            "sentiment": {
                "document": True
            }
        }
    }
}

# Select active endpoint
ACTIVE_ENDPOINT = PUBLIC_WATSON_ENDPOINT if USE_PUBLIC_WATSON else COURSERA_ENDPOINT

def get_watson_config():
    """Get the active Watson API configuration"""
    return ACTIVE_ENDPOINT

def format_watson_response(response_text, is_public_api=False):
    """
    Format Watson response to a consistent format
    
    Args:
        response_text: Raw response from Watson API
        is_public_api: Whether the response is from public Watson API
        
    Returns:
        Formatted response dict
    """
    import json
    
    try:
        response_data = json.loads(response_text)
        
        if is_public_api and 'sentiment' in response_data:
            # Convert public API format to Coursera format
            sentiment = response_data['sentiment']['document']
            return json.dumps({
                "documentSentiment": {
                    "label": sentiment.get('label', 'neutral'),
                    "score": sentiment.get('score', 0.0)
                }
            })
        
        return response_text
    except json.JSONDecodeError:
        return response_text
