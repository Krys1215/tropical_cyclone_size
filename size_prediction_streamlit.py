import streamlit as st
import pandas as pd
import folium
import pickle
import sklearn
from streamlit_folium import st_folium
import os

st.write("""
# Tropical Cyclone Size Prediction         
Select your Latitude, Longitude, Pressure, and Wind Speed data to predict!
""")

# read the model
path = os.path.dirname(__file__)
model_file = path + '\\rf_regressor.pkl'
model = pickle.load(open(model_file,'rb'))


latitude = st.slider("Latitude", 0, 49)
longitude = st.slider("Longitude", 100 , 180)
pressure = st.slider("Pressure", 700 , 1200)
wind_speed = st.slider("Wind Speed", 10, 80)


row = [[latitude,longitude,pressure,wind_speed]]
size = float(model.predict(row))

maps = folium.Map(location=[latitude, longitude], zoom_start= 6)

folium.Circle(
    location=[latitude, longitude], # lat and lon from chosen row
    radius= size * 1000, # times 1000 to match the real scale
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity=0.2
).add_to(maps)

st_data = st_folium(maps)