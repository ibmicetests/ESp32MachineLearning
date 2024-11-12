import sys
import joblib
import numpy as np

def predict_weather(temperature, humidity, wind_speed, pressure):
    # Load model and scaler
    model = joblib.load('weather_model.pkl')
    scaler = joblib.load('scaler.pkl')
    
    # Prepare input data
    input_data = np.array([[temperature, humidity, wind_speed, pressure]])
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    return prediction

if __name__ == "__main__":
    # Get arguments from command line
    temperature = float(sys.argv[1])
    humidity = float(sys.argv[2])
    wind_speed = float(sys.argv[3])
    pressure = float(sys.argv[4])
    
    # Make prediction and print result
    result = predict_weather(temperature, humidity, wind_speed, pressure)
    print(result) 