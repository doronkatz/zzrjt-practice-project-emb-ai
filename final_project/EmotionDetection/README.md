# EmotionDetection Package

A Python package for emotion detection using IBM Watson Natural Language Processing service.

## Features

- Analyze text to detect emotions (anger, disgust, fear, joy, sadness)
- Get dominant emotion from text
- Command-line interface for quick analysis
- Backward compatibility with sentiment analysis

## Installation

```bash
pip install EmotionDetection
```

Or install from source:

```bash
git clone https://github.com/doronkatz/zzrjt-practice-project-emb-ai.git
cd zzrjt-practice-project-emb-ai/final_project
pip install .
```

## Usage

### As a Python Module

```python
from EmotionDetection import emotion_detector

# Analyze text
result = emotion_detector("I am so happy I am doing this!")

# Result format:
# {
#     'anger': 0.004,
#     'disgust': 0.000,
#     'fear': 0.004,
#     'joy': 0.992,
#     'sadness': 0.014,
#     'dominant_emotion': 'joy'
# }
```

### Command Line Interface

```bash
# Get JSON output (default)
emotion-detector "I am so happy I am doing this!"

# Get formatted human-readable output
emotion-detector "I am so happy I am doing this!" --formatted
```

## Configuration

The package requires IBM Watson NLP credentials. Set up your environment variable:

```bash
export WATSON_API_KEY="your-api-key-here"
```

## Requirements

- Python 3.8+
- requests>=2.25.0

## License

Apache License 2.0
