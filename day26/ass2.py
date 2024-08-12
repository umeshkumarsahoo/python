weather_c={
    "monday":32,
    "tuesday":45,
    "wednesday":40,
    "friday":36,
    "saturday":39,
    "sunday":42,
}
weather_report={days:str(round(c*(9/5)+32,2))+"f" for (days,c) in weather_c.items()}
print(weather_report)
