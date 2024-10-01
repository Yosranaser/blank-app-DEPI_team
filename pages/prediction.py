import streamlit as st
import pickle
import numpy as np
# Load the saved model
model_filename = '/mnt/data/model (3).pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

def main():
    st.title("Churn Prediction")

    # Take input for all 19 features
    st.write("### Enter Customer Information")

    # Example features - you need to adjust this according to your dataset
    tenure = st.number_input("Tenure (Number of months the customer has stayed with the company)", min_value=0, max_value=100)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0)
    contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])

    # Add more input fields based on the features the model was trained on
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
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])

    # Convert categorical data to numerical format as needed
    contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
    payment_method_mapping = {
        'Electronic check': 0, 'Mailed check': 1, 'Bank transfer': 2, 'Credit card': 3
    }
    paperless_billing_mapping = {'Yes': 1, 'No': 0}
    senior_citizen_mapping = {'Yes': 1, 'No': 0}
    gender_mapping = {'Male': 1, 'Female': 0}
    partner_mapping = {'Yes': 1, 'No': 0}
    dependents_mapping = {'Yes': 1, 'No': 0}
    phone_service_mapping = {'Yes': 1, 'No': 0}
    multiple_lines_mapping = {'Yes': 1, 'No': 0, 'No phone service': 2}
    internet_service_mapping = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
    online_security_mapping = {'Yes': 1, 'No': 0, 'No internet service': 2}
    online_backup_mapping = {'Yes': 1, 'No': 0, 'No internet service': 2}
    device_protection_mapping = {'Yes': 1, 'No': 0, 'No internet service': 2}
    tech_support_mapping = {'Yes': 1, 'No': 0, 'No internet service': 2}
    streaming_tv_mapping = {'Yes': 1, 'No': 0, 'No internet service': 2}
    streaming_movies_mapping = {'Yes': 1, 'No': 0, 'No internet service': 2}

    # Prepare the input array based on all features
    input_data = np.array([[tenure, monthly_charges, total_charges,
                            contract_mapping[contract], paperless_billing_mapping[paperless_billing],
                            payment_method_mapping[payment_method], senior_citizen_mapping[senior_citizen],
                            gender_mapping[gender], partner_mapping[partner], dependents_mapping[dependents],
                            phone_service_mapping[phone_service], multiple_lines_mapping[multiple_lines],
                            internet_service_mapping[internet_service], online_security_mapping[online_security],
                            online_backup_mapping[online_backup], device_protection_mapping[device_protection],
                            tech_support_mapping[tech_support], streaming_tv_mapping[streaming_tv],
                            streaming_movies_mapping[streaming_movies]]])

    if st.button("Predict Churn"):
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("The model predicts that this customer is likely to churn.")
        else:
            st.success("The model predicts that this customer is unlikely to churn.")

if __name__ == "__main__":
    main()
