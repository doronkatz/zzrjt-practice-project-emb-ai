#!/usr/bin/env python3
"""Example usage of the sentiment analyzer"""

from final_project import sentiment_analyzer
import json

def main():
    print("Sentiment Analysis Example\n")
    
    # Example text
    text = "I really enjoyed using this product. It works great!"
    
    print(f"Analyzing text: '{text}'")
    print("-" * 60)
    
    # Analyze sentiment using Watson NLP
    result = sentiment_analyzer(text)
    
    # Parse and display the result
    try:
        result_dict = json.loads(result)
        
        if "error" in result_dict:
            print(f"Error: {result_dict['error']}")
        else:
            print(f"Result: {json.dumps(result_dict, indent=2)}")
            
            # Extract key information
            if "documentSentiment" in result_dict:
                sentiment = result_dict["documentSentiment"]["label"]
                score = result_dict["documentSentiment"]["score"]
                print(f"\nSentiment: {sentiment}")
                print(f"Score: {score}")
    
    except json.JSONDecodeError:
        print(f"Raw response: {result}")

if __name__ == "__main__":
    main()
