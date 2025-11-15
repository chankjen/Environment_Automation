# src/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    env = os.getenv('ENVIRONMENT', 'development')
    return jsonify({
        'message': 'Hello from CI/CD Pipeline!',
        'environment': env,
        'status': 'healthy'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)