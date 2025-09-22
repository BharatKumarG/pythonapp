from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    """Health check endpoint for CI/CD pipeline"""
    return jsonify({
        "status": "healthy",
        "service": "simple-python-app",
        "version": "1.0.0",
        "environment": os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to the Simple Python App!",
        "endpoints": [
            "/health - Health check",
            "/ - This endpoint"
        ]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
