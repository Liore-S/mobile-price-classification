import streamlit as st

import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

st.title('Mobile Price Range Prediction')

battery = st.number_input('Battery Power', min_value=500, max_value=2000, value=1000)
touchScreen = st.selectbox('Touch Screen', (0, 1))
int_memory = st.slider('Internal Memory', min_value=2, max_value=65, value=30)
mobile_wt = st.slider('Mobile Weight', min_value=80, max_value=200, value=135)
pc = st.slider('Primary Camera', min_value=0, max_value=20, value=10)
px_height = st.slider('Pixel Height', min_value=1, max_value=1920, value=1000)
px_width = st.slider('Pixel Width', min_value=1, max_value=2000, value=1000)
ram = st.slider('RAM', min_value=200, max_value=4000, value=2200)
sc_h = st.slider('Screen Height', min_value=1, max_value=20, value=10)
sc_w = st.slider('Screen Width', min_value=1, max_value=20, value=10)

def predict():
    row = np.array([battery, touchScreen, int_memory, mobile_wt, pc, px_height, px_width, ram, sc_h, sc_w])
    row = row.reshape(1, -1)
    prediction = model.predict(row)
    if (prediction == 0):
        st.info('Price Range 0')
    elif (prediction == 1):
        st.info('Price Range 1')
    elif (prediction == 2):
        st.info('Price Range 2')
    elif (prediction == 3):
        st.info('Price Range 3')

st.button('Predict', on_click=predict)