# Emotion Detection with Watson NLP

This project implements an emotion/sentiment analysis application using IBM Watson's Natural Language Processing service with Flask as the web framework. It includes automatic fallback to a mock analyzer for testing and development purposes.

## 🚀 Features

- **Watson NLP Integration**: Leverages IBM Watson's Natural Language Processing service for accurate sentiment analysis
- **Automatic Fallback**: Includes a mock sentiment analyzer that activates when Watson service is unavailable
- **Web Interface**: Flask-based web application for easy interaction
- **Comprehensive Testing**: Includes test suites for both real and mock analyzers
- **Error Handling**: Robust error handling with graceful degradation

## 📋 Prerequisites

- Python 3.7+
- IBM Watson NLP service credentials (optional - the app works with mock analyzer if not available)
- Flask framework

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/doronkatz/zzrjt-practice-project-emb-ai.git
cd zzrjt-practice-project-emb-ai
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask requests
```

4. Set up Watson API credentials (optional):
```bash
export WATSON_API_KEY="your-watson-api-key"
```

## 📁 Project Structure

```
.
├── README.md                    # This file
├── watson_config.py            # Watson API configuration
├── server.py                   # Flask web server (to be completed)
├── example_usage.py            # Example usage script
└── final_project/
    ├── emotion_detection.py    # Main emotion detection module
    ├── test_sentiment.py       # Comprehensive test suite
    └── test_mock_sentiment.py  # Mock analyzer test suite
```

## 🔧 Configuration

The project uses `watson_config.py` to manage Watson API settings. The configuration supports both:
- **Public Watson API**: Requires authentication with API key
- **Local/Private Watson instance**: For development environments

## 💻 Usage

### Command Line Example

```python
from final_project.emotion_detection import analyze_sentiment_with_fallback

text = "I love this amazing product!"
result = analyze_sentiment_with_fallback(text)
print(result)
```

### Running Tests

```bash
# Test the complete functionality
cd final_project
python3 test_sentiment.py

# Test mock analyzer only
python3 test_mock_sentiment.py
```

### Example Output

```json
{
  "documentSentiment": {
    "label": "positive",
    "score": 0.992391
  }
}
```

## 🧪 Mock Analyzer

When Watson service is unavailable, the system automatically falls back to a rule-based mock analyzer that:
- Performs keyword-based sentiment analysis
- Returns results in the same format as Watson
- Includes a "mock" flag to indicate fallback usage

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 TODO

- [ ] Complete Flask web interface in `server.py`
- [ ] Add HTML templates for the web interface
- [ ] Implement additional emotion categories beyond positive/negative/neutral
- [ ] Add support for batch text processing
- [ ] Create Docker container for easy deployment

## 🐛 Troubleshooting

### Module Import Errors
If you encounter import errors, ensure you're running scripts from the project root directory and that the parent directory is in your Python path.

### Watson API Connection Issues
The application will automatically use the mock analyzer if Watson service is unavailable. Check your API credentials and network connectivity if you need the Watson service.

## 📄 License

This project is part of the IBM Developer Skills Network Coursera course on Python and Flask.

## 🙏 Acknowledgments

- IBM Watson Natural Language Processing team
- Coursera and IBM Developer Skills Network for the project framework
- Flask community for the excellent web framework
