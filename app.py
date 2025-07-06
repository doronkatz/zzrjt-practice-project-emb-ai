#!/usr/bin/env python3
"""
Main Flask application for Emotion Detection service.

This application provides a web interface and API endpoints for emotion/sentiment analysis
using IBM Watson NLP service.
"""

from flask import Flask, render_template, request, jsonify
from final_project import emotion_detector
import json

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Render the main application page.
    
    Returns:
        HTML template for the main page
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """
    API endpoint for emotion detection.
    
    Accepts JSON or form data with 'text' field and returns emotion analysis results.
    
    Returns:
        JSON response with emotion analysis results or error message
    """
    try:
        # Get text from request (support both JSON and form data)
        if request.is_json:
            text_to_analyze = request.json.get('text', '')
        else:
            text_to_analyze = request.form.get('text', '')
        
        # Validate input
        if not text_to_analyze or text_to_analyze.strip() == '':
            return jsonify({
                'error': 'No text provided for analysis',
                'status': 'error'
            }), 400
        
        # Perform emotion detection
        result = emotion_detector(text_to_analyze)
        
        # Check if result is a dict (success) or string (error)
        if isinstance(result, dict):
            # Successful analysis
            return jsonify({
                'status': 'success',
                'emotions': result
            }), 200
        else:
            # Result is a JSON string, likely an error
            try:
                result_dict = json.loads(result)
                
                # Check if there was an error from the emotion detector
                if 'error' in result_dict:
                    return jsonify({
                        'error': result_dict['error'],
                        'status': 'error',
                        'details': result_dict.get('details', '')
                    }), 503
                else:
                    # Unknown format
                    return jsonify({
                        'status': 'success',
                        'data': result_dict
                    }), 200
                    
            except json.JSONDecodeError:
                # If result is not JSON, return it as-is
                return jsonify({
                    'status': 'error',
                    'error': 'Invalid response format',
                    'raw_response': result
                }), 500
            
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'error': f'Internal server error: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
        JSON response indicating service health
    """
    return jsonify({
        'status': 'healthy',
        'service': 'Emotion Detection API',
        'version': '1.0.0'
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 'error'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'error': 'Internal server error',
        'status': 'error'
    }), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
