
import requests
API_KEY='a3b90bb8f1e24e74169b7ac4a494d814'
city_id=""
def get_data(place='London',forecast_days=1):
  
  url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
  response=requests.get(url)
  data=response.json()
  num=forecast_days*8 
  if data and response.status_code==200:
    data_main=data['list'][:num]
    
    dates=[item['dt_txt'] for item in data_main ]
    temps=[item['main']['temp'] for item in data_main]
    temps=[round(temp/10,2) for temp in temps]
    sky=[item['weather'][0]['main'] for item in data_main]
    
    
    return data_main,dates,temps,sky
  else:
    return 0,0,0,0

if __name__=='__main__':
  data,dates,temps,sky=get_data('London',forecast_days=2)
  print(data)
  print(len(data))
  print(dates)
  print(temps)
  print(sky)