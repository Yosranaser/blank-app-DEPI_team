import streamlit as st
import pickle
import numpy as np

# Load the saved model
model_filename = '/mnt/data/model (3).pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

def main():
    # Set title for the page
    st.title("Churn Prediction")

    # Take user input for features required by the model
    st.write("### Enter Customer Information")

    # Assuming the model expects these features:
    tenure = st.number_input("Tenure (Number of months the customer has stayed with the company)", min_value=0, max_value=100)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0)
    contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])

    # Convert categorical data to numerical format for the model
    contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
    payment_method_mapping = {
        'Electronic check': 0, 'Mailed check': 1, 'Bank transfer': 2, 'Credit card': 3
    }
    paperless_billing_mapping = {'Yes': 1, 'No': 0}

    # Transform inputs as per model's requirement
    contract_num = contract_mapping[contract]
    payment_method_num = payment_method_mapping[payment_method]
    paperless_billing_num = paperless_billing_mapping[paperless_billing]

    # Prepare the input for the model
    input_data = np.array([[tenure, monthly_charges, total_charges, contract_num, paperless_billing_num, payment_method_num]])

    # Make predictions when the user clicks the button
    if st.button("Predict Churn"):
        prediction = model.predict(input_data)

        # Display the result to the user
        if prediction[0] == 1:
            st.error("The model predicts that this customer is likely to churn.")
        else:
            st.success("The model predicts that this customer is unlikely to churn.")

if __name__ == "__main__":
    main()
