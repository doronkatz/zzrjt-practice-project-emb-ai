#!/usr/bin/env python3
"""Test script for sentiment_analysis.py"""

from emotion_detection import emotion_detector as sentiment_analyzer, mock_sentiment_analyzer, analyze_sentiment_with_fallback
import json

def test_sentiment_analysis():
    print("Testing Sentiment Analysis Functions\n")
    
    # Test texts
    test_texts = [
        "I love this movie! It's absolutely fantastic!",
        "This is terrible. I hate it.",
        "The weather is okay today.",
        "This product is good but could be better."
    ]
    
    print("1. Testing original sentiment_analyzer with error handling:")
    print("-" * 60)
    for text in test_texts:
        print(f"\nText: '{text}'")
        result = sentiment_analyzer(text)
        print(f"Result: {result}")
    
    print("\n\n2. Testing mock_sentiment_analyzer:")
    print("-" * 60)
    for text in test_texts:
        print(f"\nText: '{text}'")
        result = mock_sentiment_analyzer(text)
        result_dict = json.loads(result)
        print(f"Sentiment: {result_dict['documentSentiment']['label']}")
        print(f"Score: {result_dict['documentSentiment']['score']}")
    
    print("\n\n3. Testing analyze_sentiment_with_fallback (auto-fallback):")
    print("-" * 60)
    for text in test_texts:
        print(f"\nText: '{text}'")
        result = analyze_sentiment_with_fallback(text)
        print(f"Result: {result}")
    
    print("\n\n4. Testing analyze_sentiment_with_fallback (forced mock):")
    print("-" * 60)
    text = "This is an amazing product!"
    print(f"\nText: '{text}'")
    result = analyze_sentiment_with_fallback(text, use_mock=True)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_sentiment_analysis()
