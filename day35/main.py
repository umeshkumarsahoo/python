import  tkinter as tk
from turtle import Turtle
import requests as req
url="https://api.openweathermap.org/data/2.5"
api="15987d040e20e5c1cbb729900c036cea"
weather_params={
"lat":20.765221,
"lon":86.175179,
"appid":api,
"exclude":"current,minute,daily"
}
response=req.get(url,params=weather_params)
response.raise_for_status()
data=response.json()
print(data)
