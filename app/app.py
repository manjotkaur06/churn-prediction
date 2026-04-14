import gradio as gr
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

def predict(tenure, monthly_charges, total_charges):
    features = np.array([[tenure, monthly_charges, total_charges]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        return "⚠️ Customer will churn"
    else:
        return "✅ Customer will NOT churn"

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Tenure"),
        gr.Number(label="Monthly Charges"),
        gr.Number(label="Total Charges")
    ],
    outputs="text",
    title="Customer Churn Prediction",
    description="Predict if a customer will leave the service"
)

demo.launch()