# 🔍 Multicollinearity Analyzer for Numeric Datasets

Check out the live app 👉 [Click to View the App](https://multicollinearityfor-any-datset-uip3qbn8uspszwxvnt85h8.streamlit.app/)]

## 📌 Project Overview

This Streamlit web app helps data scientists and analysts quickly **identify multicollinearity** in numeric features of a dataset. Multicollinearity can significantly affect regression models, leading to unstable coefficients and poor interpretability.

The tool computes:
- **Correlation Matrix**
- **Variance Inflation Factor (VIF)** for all numeric columns
- Highlighted features with high multicollinearity (VIF > 10)

## 🧠 Why this matters?

In real-world ML projects, especially in regression tasks, high multicollinearity among features can:
- Distort model interpretations
- Reduce the reliability of coefficient estimates
- Affect prediction performance

This tool helps detect and address such issues early in the model-building process.

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy, Statsmodels**
- **Streamlit** (for UI)

## 🚀 Features

- Upload your dataset (CSV)
- Automatically detects numeric features
- Calculates pairwise correlations
- Displays VIF scores for all numeric variables
- Highlights high VIF columns for easy identification

