import streamlit as st
import pandas as pd
import joblib


# Load trained model

model = joblib.load(
    r"C:\Users\hp\OneDrive\Desktop\Diabetes Risk Prediction\notebooks\diabetes_model.pkl"
)

# Page title
st.title("Diabetes Risk Prediction")

st.write(
    "Enter the patient's information to get a machine learning prediction."
)


# User inputs
pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function"
)
age = st.number_input("Age")


# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree],
        "Age": [age]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Higher diabetes risk")
    else:
        st.success("Lower diabetes risk")