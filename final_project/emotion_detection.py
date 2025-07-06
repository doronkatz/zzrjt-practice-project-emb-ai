import requests
import json
import os
import sys
sys.path.append('..')  # Add parent directory to path
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError, Timeout, RequestException
from watson_config import get_watson_config, format_watson_response, USE_PUBLIC_WATSON

def emotion_detector(text_to_analyse, use_fallback=True):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    """Analyze emotion of the given text using Watson NLP service.

    Args:
        text_to_analyse (str): The text to analyze
        use_fallback (bool): Whether to use mock analyzer on connection failure (default: True)
        
    Returns:
        str: JSON response from the sentiment analysis service or mock analyzer
    """
    # Get Watson API configuration
    config = get_watson_config()
    api_url = config["url"]
    header = config["headers"]
    myobj = config["payload_format"](text_to_analyse)
    
    try:
        # Add authentication for public Watson API
        if USE_PUBLIC_WATSON:
            auth = HTTPBasicAuth('apikey', os.environ.get('WATSON_API_KEY', ''))
            response = requests.post(api_url, json=myobj, headers=header, auth=auth, timeout=10)
        else:
            response = requests.post(api_url, json=myobj, headers=header, timeout=10)  # Send a POST request to the API with the text and headers and a timeout
        response.raise_for_status()  # Raise an exception for bad status codes
        # Format the response consistently
        return format_watson_response(response.text, USE_PUBLIC_WATSON)
    except ConnectionError as e:
        # Handle connection errors
        error_msg = f"Connection Error: Unable to reach the sentiment analysis service. The service may be down or unreachable from your network."
        print(error_msg)
        if use_fallback:
            print("Using mock sentiment analyzer as fallback...")
            return mock_sentiment_analyzer(text_to_analyse)
        return json.dumps({"error": error_msg, "details": str(e)})
    except Timeout as e:
        # Handle timeout errors
        error_msg = "Timeout Error: The request to the sentiment analysis service timed out."
        print(error_msg)
        if use_fallback:
            print("Using mock sentiment analyzer as fallback...")
            return mock_sentiment_analyzer(text_to_analyse)
        return json.dumps({"error": error_msg, "details": str(e)})
    except RequestException as e:
        # Handle other request errors
        error_msg = f"Request Error: An error occurred while making the request."
        print(error_msg)
        if use_fallback:
            print("Using mock sentiment analyzer as fallback...")
            return mock_sentiment_analyzer(text_to_analyse)
        return json.dumps({"error": error_msg, "details": str(e)})
    except Exception as e:
        # Handle any other unexpected errors
        error_msg = f"Unexpected Error: {type(e).__name__}"
        print(error_msg)
        if use_fallback:
            print("Using mock sentiment analyzer as fallback...")
            return mock_sentiment_analyzer(text_to_analyse)
        return json.dumps({"error": error_msg, "details": str(e)})

# Optional: Add a mock sentiment analyzer for testing when the service is unavailable
def mock_sentiment_analyzer(text_to_analyse):
    """Mock sentiment analyzer for testing purposes when the actual service is unavailable.
    
    This provides a simple rule-based sentiment analysis as a fallback.
    """
    # Simple keyword-based sentiment analysis
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'best', 'happy']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'worst', 'horrible', 'disappointing', 'poor']
    
    text_lower = text_to_analyse.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        sentiment = "positive"
        score = min(positive_count * 0.2, 1.0)
    elif negative_count > positive_count:
        sentiment = "negative"
        score = -min(negative_count * 0.2, 1.0)
    else:
        sentiment = "neutral"
        score = 0.0
    
    # Return a response similar to what Watson might return
    return json.dumps({
        "documentSentiment": {
            "label": sentiment,
            "score": score
        },
        "mock": True,
        "message": "This is a mock response for testing purposes"
    })

# Alias for backward compatibility with tests
def sentiment_analyzer(text_to_analyse, use_fallback=True):
    """Alias for emotion_detector to maintain compatibility with tests."""
    return emotion_detector(text_to_analyse, use_fallback)

# Function to use either real or mock analyzer based on availability
def analyze_sentiment_with_fallback(text_to_analyse, use_mock=False):
    """Analyze sentiment with automatic fallback to mock analyzer if service is unavailable.
    
    Args:
        text_to_analyse (str): The text to analyze
        use_mock (bool): Force use of mock analyzer
        
    Returns:
        str: JSON response from sentiment analysis
    """
    if use_mock:
        return mock_sentiment_analyzer(text_to_analyse)
    
    result = sentiment_analyzer(text_to_analyse)
    
    # Check if the result contains an error
    try:
        result_dict = json.loads(result)
        if "error" in result_dict:
            print("Falling back to mock sentiment analyzer...")
            return mock_sentiment_analyzer(text_to_analyse)
    except json.JSONDecodeError:
        # If it's not JSON, it might be a valid response from Watson
        pass
    
    return result
