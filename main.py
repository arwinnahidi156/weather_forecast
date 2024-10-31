import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')

place=st.text_input('Place : ')
place=place.title()

days=st.slider(label='Forecast Days',min_value=1,max_value=5,help="Select the number of forecasted days.")
option='Temperature'
option=st.selectbox(label='select Data to view',options=('Temperature','Sky'))

st.subheader(f"{option} for the next {days} days in {place.title()}.")

if place and days:
  
  data,dates,temps,sky=get_data(place,days)
  
  if data !=0:

    if option=='Temperature':
      figure=px.line(x=dates,y=temps,labels={'x':'Date','y':'Temperature (C)'})
      st.plotly_chart(figure_or_data=figure)
    
    if option=='Sky':
      images={'Clear':'images/clear.png','Clouds':'images/cloud.png','Snow':'images/snow.png','Rain':'images/rain.png'}
      
      image_paths=[images[item] for item in sky]
      st.image(image_paths,width=100)
      # for item in sky:
      #   match item:
          
      #     case 'Clouds':
      #       st.image('images/cloud.png',width=100,clamp=True)
          
      #     case 'Clear':
      #       st.image('images/clear.png',width=100)
      #     case 'Rain':
      #       st.image('images/rain.png',width=100)
      #     case 'Snow':
      #       st.image('images/snow.png',width=100)
          
      