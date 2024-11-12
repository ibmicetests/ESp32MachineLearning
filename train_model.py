import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv('weather_data.csv')

# Prepare features and target
X = df[['temperature', 'humidity', 'wind_speed', 'pressure']]
y = df['weather']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the model and scaler
joblib.dump(model, 'weather_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Print accuracy
print(f"Model accuracy: {model.score(X_test_scaled, y_test):.2f}") 