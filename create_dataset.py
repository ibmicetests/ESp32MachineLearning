import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
n_samples = 1000

data = {
    'temperature': np.random.uniform(10, 35, n_samples),  # Temperature in Celsius
    'humidity': np.random.uniform(30, 95, n_samples),     # Humidity in %
    'wind_speed': np.random.uniform(0, 30, n_samples),    # Wind speed in km/h
    'pressure': np.random.uniform(980, 1025, n_samples),  # Pressure in hPa
    'weather': []
}

# Generate weather conditions based on temperature and humidity
for i in range(n_samples):
    temp = data['temperature'][i]
    humidity = data['humidity'][i]
    
    if temp > 30 and humidity < 50:
        weather = 'Sunny'
    elif temp > 25 and humidity > 70:
        weather = 'Rain'
    elif humidity > 80:
        weather = 'Drizzle'
    elif temp < 20:
        weather = 'Cloudy'
    else:
        weather = 'Sunny'
    
    data['weather'].append(weather)

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('weather_data.csv', index=False)
print("Dataset created successfully!") 