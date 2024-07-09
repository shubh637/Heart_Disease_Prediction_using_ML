import pandas as pd
import streamlit as st

# Assuming you have defined your DataFrame `df` somewhere in your code
df = pd.DataFrame({
    "Pregnancies": [1],
    "Glucose": [2],
    "BloodPressure": [2],
    "SkinThickness": [2],
    "Insulin": ["Insulin"],
    "BMI": [3],
    "DiabetesPedigreeFunction": [6],
    "Age": [5]
})

# Display the DataFrame using Streamlit
st.title("My DataFrame Example")
st.dataframe(df)
