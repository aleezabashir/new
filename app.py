import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('house_price_model.pkl')

st.title("House Price Prediction")

# User inputs
location = st.selectbox("Location", ["Downtown", "Suburb", "Countryside"])
area = st.number_input("Area (sqft)", 500, 5000, 1200)
bedrooms = st.number_input("Bedrooms", 1, 5, 3)
bathrooms = st.number_input("Bathrooms", 1, 3, 2)
floors = st.number_input("Floors", 1, 2, 1)
year_built = st.number_input("Year Built", 1950, 2023, 2010)
garage = st.selectbox("Garage", ["Yes","No"])

# Predict button
if st.button("Predict Price"):
    df = pd.DataFrame({
        'Area':[area],
        'Bedrooms':[bedrooms],
        'Bathrooms':[bathrooms],
        'Floors':[floors],
        'Year_Built':[year_built],
        'Location_Suburb':[1 if location=='Suburb' else 0],
        'Location_Downtown':[1 if location=='Downtown' else 0],
        'Garage_Yes':[1 if garage=='Yes' else 0]
    })
    price = model.predict(df)[0]
    st.success(f"Estimated House Price: ${price:,.0f}")
