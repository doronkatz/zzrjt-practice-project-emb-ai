#!/usr/bin/env python3
"""
Emotion Detection module using IBM Watson NLP.

This module can be run from the command line to analyze text sentiment.
"""

import requests
import json
import os
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError, Timeout, RequestException

# Try to import watson_config from parent directory or current directory
try:
    from ..watson_config import get_watson_config, format_watson_response, USE_PUBLIC_WATSON
except ImportError:
    # If running as a script or watson_config is in the same directory
    import sys
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    from watson_config import get_watson_config, format_watson_response, USE_PUBLIC_WATSON

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    """Analyze emotion of the given text using Watson NLP service.

    Args:
        text_to_analyse (str): The text to analyze
        
    Returns:
        str: JSON response from the sentiment analysis service
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
        
        # Parse the Watson response
        response_data = json.loads(response.text)
        
        # Extract emotion scores from Watson response
        if 'emotion' in response_data and 'document' in response_data['emotion']:
            emotions = response_data['emotion']['document']['emotion']
            
            # Find the dominant emotion
            dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
            
            # Return in the required format
            return {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
        else:
            # If emotion data is not available, return zeros
            return {
                'anger': 0,
                'disgust': 0,
                'fear': 0,
                'joy': 0,
                'sadness': 0,
                'dominant_emotion': 'none'
            }
    except ConnectionError as e:
        # Handle connection errors
        error_msg = f"Connection Error: Unable to reach the sentiment analysis service. The service may be down or unreachable from your network."
        print(error_msg)
        return json.dumps({"error": error_msg, "details": str(e)})
    except Timeout as e:
        # Handle timeout errors
        error_msg = "Timeout Error: The request to the sentiment analysis service timed out."
        print(error_msg)
        return json.dumps({"error": error_msg, "details": str(e)})
    except RequestException as e:
        # Handle other request errors
        error_msg = f"Request Error: An error occurred while making the request."
        print(error_msg)
        return json.dumps({"error": error_msg, "details": str(e)})
    except Exception as e:
        # Handle any other unexpected errors
        error_msg = f"Unexpected Error: {type(e).__name__}"
        print(error_msg)
        return json.dumps({"error": error_msg, "details": str(e)})

# Alias for backward compatibility with tests
def sentiment_analyzer(text_to_analyse):
    """Alias for emotion_detector to maintain compatibility with tests.
    
    Converts emotion analysis to sentiment format for backward compatibility.
    """
    result = emotion_detector(text_to_analyse)
    
    # If it's already a string (error), return as-is
    if isinstance(result, str):
        return result
    
    # Convert emotion to sentiment based on dominant emotion
    if result['dominant_emotion'] in ['joy']:
        sentiment = 'positive'
        score = result['joy']
    elif result['dominant_emotion'] in ['anger', 'disgust', 'fear', 'sadness']:
        sentiment = 'negative'
        # Use the dominant negative emotion's score
        score = -result[result['dominant_emotion']]
    else:
        sentiment = 'neutral'
        score = 0.0
    
    return json.dumps({
        "documentSentiment": {
            "label": sentiment,
            "score": score
        }
    })

def main():
    """Main function to run emotion detection from command line."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Analyze emotion/sentiment of text using Watson NLP',
        epilog='Example: python emotion_detection.py "I love this product!"'
    )
    parser.add_argument(
        'text',
        type=str,
        help='Text to analyze for emotion/sentiment'
    )
    parser.add_argument(
        '--formatted',
        action='store_true',
        help='Output formatted human-readable response instead of JSON'
    )
    
    args = parser.parse_args()
    
    # Analyze the text
    result = emotion_detector(args.text)
    
    # emotion_detector now returns a dict or JSON string (for errors)
    try:
        # Check if result is already a dict (success case)
        if isinstance(result, dict):
            result_dict = result
        else:
            # It's a JSON string (error case)
            result_dict = json.loads(result)
        
        if args.formatted:
            # Format the output nicely
            if 'error' in result_dict:
                print(f"\n❌ Error: {result_dict['error']}")
                if 'details' in result_dict:
                    print(f"   Details: {result_dict['details']}")
            elif 'dominant_emotion' in result_dict:
                # Display emotion analysis results
                dominant = result_dict['dominant_emotion']
                
                # Emoji based on dominant emotion
                emotion_emojis = {
                    'joy': '😊',
                    'anger': '😡',
                    'disgust': '🤢',
                    'fear': '😨',
                    'sadness': '😢',
                    'none': '😐'
                }
                emoji = emotion_emojis.get(dominant, '😐')
                
                print(f"\n{emoji} Emotion Analysis Results:")
                print(f"   Text: \"{args.text}\"")
                print(f"\n   Emotion Scores:")
                print(f"     Joy:      {result_dict['joy']:.3f}")
                print(f"     Anger:    {result_dict['anger']:.3f}")
                print(f"     Disgust:  {result_dict['disgust']:.3f}")
                print(f"     Fear:     {result_dict['fear']:.3f}")
                print(f"     Sadness:  {result_dict['sadness']:.3f}")
                print(f"\n   Dominant Emotion: {dominant.capitalize()}")
            else:
                # Unknown format, print raw
                print(json.dumps(result_dict, indent=2))
        else:
            # Output raw JSON (default)
            print(json.dumps(result_dict, indent=2))
                
    except json.JSONDecodeError:
        # If it's not JSON, print as-is
        print(f"\nUnexpected response format:")
        print(result)
    except Exception as e:
        print(f"\n❌ Error processing response: {str(e)}")

if __name__ == '__main__':
    main()
