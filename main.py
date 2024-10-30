import streamlit as st


st.title('Weather Forecast for the Next Days')

place=st.text_input('Place : ')

days=st.slider(label='Forecast Days',min_value=1,max_value=5,help="Select the number of forecasted days.")

option=st.selectbox(label='select Data to view',options=('Temperature','Sky'))

st.subheader(f"{option} for the next {days} days in {place.title()}.")
