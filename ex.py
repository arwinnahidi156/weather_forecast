import streamlit as st
import plotly.express as px
import pandas as pd

st.title('In search for Happiness')
df=pd.read_csv('happy.csv')
ops=list(df.columns)

x_axis=st.selectbox(label="Select the data for the X axis.",options=ops)

y_axis=st.selectbox(label="Select the data for the Y axis.",options=ops)

st.subheader(f"{x_axis} and {y_axis}")

figure=px.scatter(x=df[x_axis],y=df[y_axis],labels={'x':f"{x_axis}",'y':f"{y_axis}"})
st.plotly_chart(figure_or_data=figure)