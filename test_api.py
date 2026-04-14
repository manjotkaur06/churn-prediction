import requests
import pickle

# Load same test data (optional best way)
# If you don't have X_test here, we'll handle below

url = "http://127.0.0.1:10000/predict"

# TEMP: dummy input (we'll fix if mismatch)
data = {
    "features": [0]*30   # placeholder (update later)
}

response = requests.post(url, json=data)

print(response.json())