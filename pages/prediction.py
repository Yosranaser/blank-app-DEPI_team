import streamlit as st
import pickle
import numpy as np
import sklearn
def main():
    st.title("Churn Prediction")

    # Upload the model file
    uploaded_model = st.file_uploader("Upload the trained model", type=["pkl"])
    
    if uploaded_model is not None:
        try:
            # Try to load the uploaded model
            model = pickle.load(uploaded_model)
            st.success("Model loaded successfully!")
            
            st.write("### Enter Customer Information")

            # Take input from the user
            tenure = st.number_input("Tenure (Number of months the customer has stayed with the company)", min_value=0, max_value=100)
            monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
            total_charges = st.number_input("Total Charges", min_value=0.0)
            contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
            paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
            payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])

            # Convert categorical data to numerical format
            contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
            payment_method_mapping = {
                'Electronic check': 0, 'Mailed check': 1, 'Bank transfer': 2, 'Credit card': 3
            }
            paperless_billing_mapping = {'Yes': 1, 'No': 0}

            # Transform inputs
            contract_num = contract_mapping[contract]
            payment_method_num = payment_method_mapping[payment_method]
            paperless_billing_num = paperless_billing_mapping[paperless_billing]

            input_data = np.array([[tenure, monthly_charges, total_charges, contract_num, paperless_billing_num, payment_method_num]])

            if st.button("Predict Churn"):
                prediction = model.predict(input_data)

                if prediction[0] == 1:
                    st.error("The model predicts that this customer is likely to churn.")
                else:
                    st.success("The model predicts that this customer is unlikely to churn.")

        except Exception as e:
            st.error(f"An error occurred while loading the model: {str(e)}")
    else:
        st.warning("Please upload a valid .pkl model file to proceed.")

if __name__ == "__main__":
    main()
