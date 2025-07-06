"""
EmotionDetection Package

A Python package for emotion detection using IBM Watson NLP service.
This package provides functionality to analyze text and detect emotions.

Main Functions:
    emotion_detector: Analyzes text and returns emotion scores with dominant emotion
    sentiment_analyzer: Legacy function for backward compatibility
"""

from .emotion_detection import emotion_detector, sentiment_analyzer

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = ["emotion_detector", "sentiment_analyzer"]
