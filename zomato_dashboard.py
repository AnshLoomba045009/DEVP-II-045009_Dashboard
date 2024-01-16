import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
zomato_data = pd.read_csv('zomato.csv', low_memory=False)

# Set up Streamlit page
st.title("Zomato Restaurants Dashboard")

# Plot: Average Rating by Restaurant Type
avg_rating_by_rest_type = zomato_data.groupby('restaurant type')['rate (out of 5)'].mean().reset_index()
fig1 = px.bar(avg_rating_by_rest_type, x='restaurant type', y='rate (out of 5)', 
              title='Average Rating by Restaurant Type', color='rate (out of 5)')

# Plot: Number of Ratings by Area
fig2 = px.scatter(zomato_data, x='area', y='num of ratings', title='Number of Ratings by Area', 
                  color='num of ratings')

# Plot: Average Cost for Two by Cuisine
fig3 = px.box(zomato_data, x='cuisines type', y='avg cost (two people)', title='Average Cost for Two by Cuisine')

# Plot: Online Order Proportion
fig4 = px.pie(zomato_data, names='online_order', title='Online Order Proportion', 
              color='online_order', color_discrete_map={'Yes':'green', 'No':'red'})

# Plot: Table Booking Proportion
fig5 = px.pie(zomato_data, names='table booking', title='Table Booking Proportion', 
              color='table booking', color_discrete_map={'Yes':'blue', 'No':'orange'})

# Plot: Rating Distribution
fig6 = px.histogram(zomato_data, x='rate (out of 5)', title='Rating Distribution', 
                    color_discrete_sequence=['indigo'])

# Plot: Average Cost by Area
avg_cost_by_area = zomato_data.groupby('area')['avg cost (two people)'].mean().reset_index()
fig7 = px.area(avg_cost_by_area, x='area', y='avg cost (two people)', title='Average Cost by Area')

# Layout for side-by-side graphs
col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)

col1, col2 = st.columns(2)
col1.plotly_chart(fig3)
col2.plotly_chart(fig4)

col1, col2 = st.columns(2)
col1.plotly_chart(fig5)
col2.plotly_chart(fig6)

col1, col2 = st.columns(2)
col1.plotly_chart(fig7)
