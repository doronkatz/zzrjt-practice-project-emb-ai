# Watson Sentiment Analysis Setup Guide

This project uses IBM Watson's Natural Language Understanding service for sentiment analysis. Due to the network configuration, you have several options to get it working:

## Current Issue

The default Watson endpoint (`sn-watson-sentiment-bert.labs.skills.network`) is only accessible from within the Coursera/IBM Skills Network. From your local machine, this endpoint is unreachable.

## Solutions

### Option 1: Use the Mock Sentiment Analyzer (Recommended for Testing)

The code automatically falls back to a mock sentiment analyzer when Watson is unreachable. This allows you to test your application without any Watson credentials.

```python
from sentiment_analysis import sentiment_analyzer

# This will automatically use the mock analyzer when Watson is unreachable
result = sentiment_analyzer("I love this technology!")
print(result)
```

### Option 2: Use IBM Watson Public API (Recommended for Production)

1. **Create an IBM Cloud Account**
   - Go to https://cloud.ibm.com
   - Sign up for a free account (no credit card required for lite plan)

2. **Create a Watson Natural Language Understanding Service**
   - In IBM Cloud dashboard, click "Create resource"
   - Search for "Natural Language Understanding"
   - Select the Lite plan (free tier)
   - Create the service

3. **Get Your Credentials**
   - Go to your NLU service instance
   - Click on "Service credentials"
   - Click "New credential" and create one
   - View the credential to see your API key and URL

4. **Configure Your Environment**
   
   Create a `.env` file in your project directory:
   ```bash
   USE_PUBLIC_WATSON=true
   WATSON_API_KEY=your-api-key-here
   WATSON_URL=https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id/v1/analyze?version=2022-04-07
   ```

   Or set environment variables in your terminal:
   ```bash
   export USE_PUBLIC_WATSON=true
   export WATSON_API_KEY="your-api-key-here"
   export WATSON_URL="https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id/v1/analyze?version=2022-04-07"
   ```

5. **Install python-dotenv (if using .env file)**
   ```bash
   pip install python-dotenv
   ```

6. **Update watson_config.py to load .env file**
   Add this at the top of watson_config.py:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Option 3: Access from Coursera Environment

If you're running this code within the Coursera lab environment, the default endpoint should work without any changes.

### Option 4: Use VPN (If Available)

If you have access to IBM's or Coursera's VPN, connecting to it should allow you to access the internal Watson endpoint.

## Testing Your Setup

Run this test script to verify your configuration:

```python
from sentiment_analysis import sentiment_analyzer
import json

# Test texts
test_texts = [
    "I absolutely love this new technology!",
    "This is terrible and disappointing.",
    "The weather is okay today."
]

for text in test_texts:
    print(f"\nAnalyzing: '{text}'")
    result = sentiment_analyzer(text)
    
    try:
        result_dict = json.loads(result)
        if "error" in result_dict:
            print(f"Error: {result_dict['error']}")
        elif "mock" in result_dict:
            print(f"Mock Result: {result_dict['documentSentiment']}")
        else:
            print(f"Watson Result: {result}")
    except:
        print(f"Raw Result: {result}")
```

## Troubleshooting

1. **"Network is unreachable" error**: You're trying to access the Coursera internal endpoint from outside their network. Use one of the solutions above.

2. **"401 Unauthorized" error**: Your Watson API key is incorrect or not set properly.

3. **"403 Forbidden" error**: Your Watson service URL might be incorrect or the service might not be provisioned.

4. **Timeout errors**: The Watson service might be slow. The timeout is set to 10 seconds but can be increased in the code.

## Support

For Coursera-specific issues, please refer to the course forums or documentation.
For IBM Watson issues, see: https://cloud.ibm.com/docs/natural-language-understanding
