import requests as req
response=req.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()
lat = data['iss_position']['latitude']
lon = data['iss_position']['longitude']
iss_pos=(lat,lon)
print(iss_pos)
