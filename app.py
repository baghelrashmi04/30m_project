import streamlit as st
import pandas as pd
import joblib

# loading the trained model
model= joblib.load("car_price_predictor_model.joblib")

st.title("🏎️ Car Price Predictor")
st.write("Enter the car details")

# user input wingets

car_age= st.slider("Car Age(years)", min_value= 1, max_value= 48, value = 5)
car_size= st.number_input("Car size metric", value= 10.0)
max_power_delivered= st.number_input("Max POwer Delivered (HP)", value=85.0)
city_freq= st.number_input("City Frequency Index", value=1.0)


# predict button

if st.button("Predict Price"):
  input_data= pd.DataFrame([[car_age,car_size,max_power_delivered,city_freq]], 
                           columns=['car_age','car_size','max_power_delivered','city_freq'])
  prediction= model.predict(input_data)[0]
  st.success(f"Estimated car price : ${prediction:,.2f}")
