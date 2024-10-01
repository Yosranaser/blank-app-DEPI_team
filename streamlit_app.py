import streamlit as st
def main():
    # Set the title of the app
    st.title("Welcome to the Churn Prediction App")

    # Introduction section
    st.write("""
    ## What does this app do?
    This app predicts customer churn using a machine learning model. Churn occurs when customers stop using a company's services or products, and predicting churn helps businesses take proactive measures to retain them.

    ## Why is this important?
    Customer retention is crucial for:
    - Reducing customer acquisition costs
    - Increasing long-term profitability
    - Identifying patterns in customer behavior that lead to churn
    - Developing targeted retention strategies for at-risk customers

    ## What will this app take from you?
    You will be asked to:
    - Upload a dataset containing customer information and their churn status (e.g., tenure, contract type, monthly charges)
    - The app will use this data to predict which customers are at risk of churning

    Let's get started! Upload your customer dataset to begin predicting churn.
    """)

if __name__ == "__main__":
    main()
