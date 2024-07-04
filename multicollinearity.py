import pandas as pd 
import streamlit as st
from statsmodels.stats.outliers_influence import variance_inflation_factor 

# Function to calculate VIF
def calculate_vif(X):
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
    return vif_data

# Function to interpret VIF results
def interpret_vif(vif_data):
    interpretation = []
    for index, row in vif_data.iterrows():
        if row['VIF'] > 10:
            interpretation.append(f"The feature '{row['Feature']}' has a VIF of {row['VIF']:.2f}, indicating high multicollinearity. Consider removing or combining this feature with others.")
        elif row['VIF'] > 5:
            interpretation.append(f"The feature '{row['Feature']}' has a VIF of {row['VIF']:.2f}, indicating moderate multicollinearity. Investigate further to see if this can be reduced.")
        else:
            interpretation.append(f"The feature '{row['Feature']}' has a VIF of {row['VIF']:.2f}, indicating low multicollinearity.")
    return interpretation

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

        # Multiselect for choosing features
        selected_features = st.multiselect("Select features for VIF calculation", options=numerical_cols, default=list(numerical_cols))

        if len(selected_features) > 0:
            X = data[selected_features]

            # Calculate VIF
            st.write("### Variance Inflation Factor (VIF)")
            vif_result = calculate_vif(X)
            st.write(vif_result)

            # Interpret VIF results
            st.write("### VIF Interpretation")
            vif_interpretation = interpret_vif(vif_result)
            for interpretation in vif_interpretation:
                st.write(interpretation)
        else:
            st.write("Please select at least one feature.")

    else:
        st.write("Please upload a valid CSV file.")
