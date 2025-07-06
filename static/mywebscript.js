let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    
    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = 
            '<div class="alert alert-warning">Please enter some text to analyze.</div>';
        return;
    }
    
    // Show loading state
    document.getElementById("system_response").innerHTML = 
        '<div class="alert alert-info">Analyzing...</div>';
    
    // Use POST method with JSON payload
    fetch('/emotionDetector', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: textToAnalyze })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success' && data.emotions) {
            const emotions = data.emotions;
            const dominant = emotions.dominant_emotion;
            
            // Choose color based on dominant emotion
            let alertColor = 'info';
            if (dominant === 'joy') alertColor = 'success';
            else if (['anger', 'fear', 'sadness', 'disgust'].includes(dominant)) alertColor = 'warning';
            
            // Format emotion scores as percentage
            const formatScore = (score) => (score * 100).toFixed(1) + '%';
            
            document.getElementById("system_response").innerHTML = `
                <div class="alert alert-${alertColor}">
                    <h4>Emotion Analysis Results</h4>
                    <div class="row mt-3">
                        <div class="col-md-6">
                            <h5>Emotion Scores:</h5>
                            <ul class="list-unstyled">
                                <li><strong>Joy:</strong> ${formatScore(emotions.joy)}</li>
                                <li><strong>Anger:</strong> ${formatScore(emotions.anger)}</li>
                                <li><strong>Disgust:</strong> ${formatScore(emotions.disgust)}</li>
                                <li><strong>Fear:</strong> ${formatScore(emotions.fear)}</li>
                                <li><strong>Sadness:</strong> ${formatScore(emotions.sadness)}</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <h5>Dominant Emotion:</h5>
                            <p class="lead"><strong>${dominant.charAt(0).toUpperCase() + dominant.slice(1)}</strong></p>
                        </div>
                    </div>
                </div>
            `;
        } else if (data.status === 'success' && data.data) {
            // Fallback for other formats
            document.getElementById("system_response").innerHTML = `
                <div class="alert alert-info">
                    <pre>${JSON.stringify(data.data, null, 2)}</pre>
                </div>
            `;
        } else if (data.status === 'error') {
            document.getElementById("system_response").innerHTML = `
                <div class="alert alert-danger">
                    <h4>Error</h4>
                    <p>${data.error}</p>
                    ${data.details ? `<small>${data.details}</small>` : ''}
                </div>
            `;
        }
    })
    .catch(error => {
        document.getElementById("system_response").innerHTML = `
            <div class="alert alert-danger">
                <h4>Connection Error</h4>
                <p>Failed to connect to the server. Please try again.</p>
            </div>
        `;
        console.error('Error:', error);
    });
}
