import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

#read CSV

car_data = pd.read_csv('notebooks/vehicles_us.csv')
st.header('US Vehicles')
st.write('This is a demo of a data science web application by Jorge Mora')

#show the Dataframe
st.header('Data viewer')
table_check= st.checkbox('Show ramdon 1000 vechicles' ,True)

if table_check:
  st.dataframe(car_data.sample(100))
else:
   st.dataframe(car_data)

st.header('Us Vehicles by Manufacturer')

#split the brand of the vehicle
brand_list = [] #empty list for the table
for brand in car_data['model']:
    brand_name=brand.split()
    brand_list.append(brand_name[0])
car_data['brand']=brand_list

#show the histogram  brand vs type

figpx = px.histogram(car_data,
                     x='brand',
                     color='type'
                     )

st.plotly_chart(figpx,use_container_width=True)

#comparation condition vs year

st.header('Condition vs Year')
car_data['brand']=brand_list

figpx = px.histogram(car_data,
                     x='model_year',
                     color='condition'
                     )
st.plotly_chart(figpx,use_container_width=True)

#compare the price vs Manufacturer with 2 selectbox

st.header('Compare price and Manufacturer')
manufacturer_1 = st.selectbox('Selec the manufacturer 1: ',
                              (car_data['brand'].value_counts().index),
                              index=None,placeholder='Select brand')
                       
manufacturer_2 = st.selectbox('Selec the manufacturer 2: ',
                              (car_data['brand'].value_counts().index),
                              index=None,placeholder='Select brand')
                       
figpx = px.histogram(car_data[car_data['brand'].isin([manufacturer_1,manufacturer_2])],
                     x='price',
                     color='brand',
                     nbins=40
                     )
st.plotly_chart(figpx,use_container_width=True)



