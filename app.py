import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('notebooks/vehicles_us.csv')
st.header('US Vehicles')
hist_button = st.button('Histogram build')
disp_button = st.button('Scatter graphich build')

if hist_button:
    '''
    Construir boton que muestre el histograma
    '''
    st.write('Build a histogram of the Data')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    '''
    Construir boton que muestre el grafico de dispersion
        
    '''
    st.write('Build scatter graphic')
    scatter_fig = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(scatter_fig,use_container_width=True)

    

