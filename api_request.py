import requests
url = 'https://api.wheretheiss.at/v1/satellites/25544'
url_ = 'http://api.open-notify.org/iss-now.json'



response = requests.get(url = url_)
#{'iss_position': {'longitude': '-120.4502', 'latitude': '-43.7946'}, 'timestamp': 1647788855, 'message': 'success'}
data = response.json()
lat, lon = data['iss_position']['latitude'], data['iss_position']['longitude']
print(f'(latitude, longitude) = ({lat}, {lon})')



#The above api is taken from
#http://open-notify.org/Open-Notify-API/ISS-Location-Now/


#For number of different error codes visit ⏬
#https://httpstatus.io/http-status-codes
