import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

car_data = pd.read_csv('notebooks/vehicles_us.csv')
st.header('US Vehicles')
st.write('This is a demo of a data science web application')

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

figpx = px.histogram(car_data,
                     x='brand',
                     color='type'
                     )

st.plotly_chart(figpx,use_container_width=True)

st.header('Condition vs Year')
car_data['brand']=brand_list

figpx = px.histogram(car_data,
                     x='model_year',
                     color='condition'
                     )
st.plotly_chart(figpx,use_container_width=True)

                       
'''
vehicle_by_bran=car_data.
fig = go.Figure()

for col in cols:
    figpx = px.scatter(df.assign(Plot=col),
                       x=col,
                       y="Score",
                       size="Population",
                       color="Continent",
                       hover_name="Country/Region",
                       hover_data=["Plot"],
                       size_max=60,
                       color_discrete_sequence=px.colors.qualitative.G10).update_traces(visible=False)
    
    fig.add_traces(figpx.data)

'''



