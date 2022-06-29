#An api with some input parameters

#The below code gives the time for the rise and sunset at your given location

#api source: https://sunrise-sunset.org/api



import requests
import datetime as dt

API = "http://api.sunrise-sunset.org/json"
LAT, LNG = 20.923019, 435.329849


required_params = {'lat': LAT, 'lng': LNG}
response = requests.get(API, params= required_params)
data = response.json()
format_ ='''
{
results: {
sunrise: "1:02:36 AM",
sunset: "1:10:24 PM",
solar_noon: "7:06:30 AM",
day_length: "12:07:48",
civil_twilight_begin: "12:41:37 AM",
civil_twilight_end: "1:31:23 PM",
nautical_twilight_begin: "12:15:53 AM",
nautical_twilight_end: "1:57:06 PM",
astronomical_twilight_begin: "11:50:05 PM",
astronomical_twilight_end: "2:22:55 PM"
},
status: "OK"
}
'''
today = dt.datetime.now()
print(f"{today.year}/{today.month}/{today.day}")
req = data['results']
for k in data['results']:
    val = data['results'][k]
    print(f'{k}: {val}')
