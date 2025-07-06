# Emotion Detection with Watson NLP

This project implements an emotion/sentiment analysis application using IBM Watson's Natural Language Processing service with Flask as the web framework.

## 🚀 Features

- **Watson NLP Integration**: Leverages IBM Watson's Natural Language Processing service for accurate sentiment analysis
- **Web Interface**: Flask-based web application for easy interaction
- **Comprehensive Testing**: Includes test suite for sentiment analysis
- **Error Handling**: Robust error handling for API connection issues

## 📋 Prerequisites

- Python 3.7+
- IBM Watson NLP service credentials
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
pip install flask requests python-dotenv
```

4. Set up Watson API credentials:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Watson API credentials:
     ```bash
     # Open .env in your editor and fill in:
     WATSON_API_KEY=your-actual-api-key
     WATSON_URL=your-actual-watson-url
     ```
   - **Important**: Never commit the `.env` file to version control!

## 📁 Project Structure

```
.
├── README.md                    # This file
├── .env.example                # Example environment variables file
├── .env                        # Your actual environment variables (DO NOT COMMIT)
├── .gitignore                  # Git ignore file (includes .env)
├── app.py                      # Main Flask application entry point
├── watson_config.py            # Watson API configuration
├── server.py                   # Flask web server (legacy)
├── example_usage.py            # Example usage script
├── templates/
│   └── index.html              # Web interface template
├── static/
│   └── mywebscript.js          # Frontend JavaScript
└── final_project/
    ├── __init__.py             # Package initialization
    ├── emotion_detection.py    # Main emotion detection module
    └── test_sentiment.py       # Comprehensive test suite
```

## 🔧 Configuration

The project uses `watson_config.py` to manage Watson API settings. The configuration supports both:
- **Public Watson API**: Requires authentication with API key
- **Local/Private Watson instance**: For development environments

## 💻 Usage

### Running the Flask Application

```bash
# Run the Flask app
python app.py
```

Then open your browser to `http://localhost:5000`

### Command Line Example

```python
from final_project import sentiment_analyzer

text = "I love this amazing product!"
result = sentiment_analyzer(text)
print(result)
```

### Running Tests

```bash
# Test the sentiment analysis functionality
cd final_project
python3 test_sentiment.py
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


## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 TODO

- [x] Complete Flask web interface with `app.py`
- [x] Add HTML templates for the web interface
- [ ] Implement additional emotion categories beyond positive/negative/neutral
- [ ] Add support for batch text processing
- [ ] Create Docker container for easy deployment
- [ ] Add API authentication
- [ ] Implement rate limiting

## 🐛 Troubleshooting

### Module Import Errors
If you encounter import errors, ensure you're running scripts from the project root directory and that the parent directory is in your Python path.

### Watson API Connection Issues
If you encounter connection errors, check your API credentials and network connectivity. Ensure the WATSON_API_KEY environment variable is properly set.

## 📄 License

This project is part of the IBM Developer Skills Network Coursera course on Python and Flask.

## 🙏 Acknowledgments

- IBM Watson Natural Language Processing team
- Coursera and IBM Developer Skills Network for the project framework
- Flask community for the excellent web framework
