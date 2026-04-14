from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, 'models', 'model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'models', 'scaler.pkl'), 'rb'))
columns = pickle.load(open(os.path.join(BASE_DIR, 'models', 'columns.pkl'), 'rb'))

@app.route('/')
def home():
    return "Churn API Running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json
        
        # Convert to DataFrame
        df = pd.DataFrame([input_data])
        
        # One-hot encoding (same as training)
        df = pd.get_dummies(df)
        
        # Align columns (CRITICAL STEP)
        df = df.reindex(columns=columns, fill_value=0)
        
        # Scale
        scaled = scaler.transform(df)
        
        # Predict
        prob = model.predict_proba(scaled)[0][1]

        return jsonify({
            'churn_probability': round(prob, 3),
            'risk_level': 'High' if prob > 0.6
                         else 'Medium' if prob > 0.35
                         else 'Low'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})
    

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 10000))
app.run(host='0.0.0.0', port=port)