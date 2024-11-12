const express = require('express');
const { spawn } = require('child_process');
const app = express();

// Use environment port or default to 3000
const port = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Basic route for testing
app.get('/', (req, res) => {
    res.send('Weather Prediction Server is running!');
});

// Prediction endpoint
app.post('/predict', async (req, res) => {
    try {
        const { temperature, humidity, wind_speed, pressure } = req.body;
        
        // Call Python script for prediction
        const python = spawn('python', [
            'predict.py',
            temperature,
            humidity,
            wind_speed,
            pressure
        ]);

        let prediction = '';

        python.stdout.on('data', (data) => {
            prediction += data.toString();
        });

        python.stderr.on('data', (data) => {
            console.error(`Error: ${data}`);
        });

        python.on('close', (code) => {
            console.log(`Prediction: ${prediction.trim()}`);
            res.json({
                prediction: prediction.trim(),
                input_data: req.body
            });
        });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
}); 