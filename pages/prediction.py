import streamlit as st
import numpy as np
import pickle

# Load your model
model_filename = '/mnt/data/model (3).pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

def main():
    st.title("Churn Prediction")

    # Input fields for 19 features (adjust based on actual features used during model training)
    st.write("### Please provide the following details:")

    # Example fields (you need to replace with actual features used during training)
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0)
    contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])
    senior_citizen = st.selectbox("Is the customer a senior citizen?", ['Yes', 'No'])
    gender = st.selectbox("Gender", ['Male', 'Female'])
    partner = st.selectbox("Has a partner", ['Yes', 'No'])
    dependents = st.selectbox("Has dependents", ['Yes', 'No'])
    phone_service = st.selectbox("Has phone service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No',

