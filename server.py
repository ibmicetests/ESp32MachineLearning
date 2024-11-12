from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and scaler
try:
    model = joblib.load('weather_model.joblib')
    scaler = joblib.load('scaler.joblib')
    print("Model and scaler loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return """
    <h1>Weather Prediction Server</h1>
    <p>Use /predict with GET or POST request</p>
    <p>Example: /predict?temperature=25&humidity=60&wind_speed=10&pressure=1013</p>
    """

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        # Handle both GET and POST requests
        if request.method == 'POST':
            data = request.get_json()
        else:  # GET request
            data = request.args

        # Extract features
        features = {
            'temperature': float(data.get('temperature')),
            'humidity': float(data.get('humidity')),
            'wind_speed': float(data.get('wind_speed')),
            'pressure': float(data.get('pressure'))
        }

        # Print received data
        print("\nReceived Data:")
        print("-" * 50)
        for key, value in features.items():
            print(f"{key}: {value}")

        # Prepare input for prediction
        input_data = np.array([[
            features['temperature'],
            features['humidity'],
            features['wind_speed'],
            features['pressure']
        ]])

        # Scale the input
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Print prediction
        print("\nPrediction:")
        print("-" * 50)
        print(f"Weather Prediction: {prediction}")

        # Prepare response
        response = {
            'prediction': prediction,
            'input_data': features
        }

        return jsonify(response)

    except Exception as e:
        error_response = {
            'error': str(e),
            'usage': 'Send temperature, humidity, wind_speed, and pressure values'
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 