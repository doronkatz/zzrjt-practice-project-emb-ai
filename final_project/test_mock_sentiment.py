#!/usr/bin/env python3
"""Simple test to demonstrate the mock sentiment analyzer"""

from emotion_detection import mock_sentiment_analyzer, analyze_sentiment_with_fallback
import json

def main():
    print("Testing Mock Sentiment Analyzer\n")
    
    # Test texts
    test_texts = [
        "I love this movie! It's absolutely fantastic!",
        "This is terrible. I hate it.",
        "The weather is okay today.",
        "This product is amazing and wonderful!"
    ]
    
    print("Using mock sentiment analyzer directly:")
    print("-" * 60)
    for text in test_texts:
        print(f"\nText: '{text}'")
        result = mock_sentiment_analyzer(text)
        result_dict = json.loads(result)
        print(f"Sentiment: {result_dict['documentSentiment']['label']}")
        print(f"Score: {result_dict['documentSentiment']['score']}")
    
    print("\n\nUsing fallback function with forced mock:")
    print("-" * 60)
    text = "This is the best product I've ever used!"
    print(f"\nText: '{text}'")
    result = analyze_sentiment_with_fallback(text, use_mock=True)
    result_dict = json.loads(result)
    print(f"Result: {json.dumps(result_dict, indent=2)}")

if __name__ == "__main__":
    main()
