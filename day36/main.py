import requests as req
import html
from twilio.rest import Client
# pre-requisites-----------------------
stock_name="TSLA"
company_name="Tesla Inc"
stock_endpoint="https://www.alphavantage.co/query"
news_endpoint="https://newsapi.org/v2/everything"
api_key="1A7JUP00TZL96AVD"#stocks
news_api="665764ba572848d784bd5009b3dd4458"
send_no="+917735203945"
from_no="+16593480984"
token="9c124897b8b708386c43ca0056078fdf"
sid="AC8e055ba191a0fd90ca0e1ccb6830784a"

news_params={
    "apiKey":news_api,
    "qInTitle":company_name
}
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":stock_name,
    "apikey":api_key,
}
#1.getting yesterday's closing stock------------
response=req.get(stock_endpoint,params=stock_params)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_closing_price=data_list[0]["4. close"]
print(data_list[0])
print(yesterday_closing_price)
#2. getting closing prices---------
day_bfr_yst=data_list[1]
day_bfr_yst_close_price=day_bfr_yst["4. close"]
print(day_bfr_yst)
print(day_bfr_yst_close_price)
#3. finding positive difference b/w 1 and 2------------>
diff=abs(float(day_bfr_yst_close_price)-float(yesterday_closing_price))
if diff>0:
    up_down="📈"
else:
    up_down="📉"
print(f"difference is {diff}")
#4. working out the percentage difference in both------->
diff_percent=(diff/float(yesterday_closing_price))*100
print(diff_percent)
#5. percentage is greater than 5---------->
if diff_percent>0:
    news_response=req.get(news_endpoint,params=news_params)
    articles=news_response.json()["articles"]
    req_articles=articles[:3]
    print(req_articles)

#6. creating list for the first 3 articles---------->
format_article=[f"{stock_name}: {up_down}{diff_percent}\nheadline:{article['title']}.\nBrief:{article['description']}" for article in req_articles]
#7. sending message using twilio----------->
client=Client(sid,token)
for article in format_article:
    message=client.messages.create(
    body=article,
    from_=from_no,
    to='+918984791744'

)
