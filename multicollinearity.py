import pandas as pd 
import streamlit as st
from statsmodels.stats.outliers_influence import variance_inflation_factor 

# Function to calculate VIF
def calculate_vif(X):
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
    return vif_data

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    data = pd.read_csv(uploaded_file)

    # Display the first five rows of the uploaded dataset
    st.write("### First Five Rows of Uploaded Dataset")
    st.table(data.head(5))

    # Check if the uploaded file is not empty
    if not data.empty:
        # Exclude non-numeric columns from VIF calculation
        numerical_cols = data.select_dtypes(include=['number']).columns
        X = data[numerical_cols]

        # Calculate VIF
        st.write("### Variance Inflation Factor (VIF)")
        vif_result = calculate_vif(X)
        st.write(vif_result)

    else:
        st.write("Please upload a valid CSV file.")
