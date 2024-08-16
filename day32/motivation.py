import smtplib
import datetime as dt
import random
my_mail="appbreweryinfo@gmail.com"
password="abcd1234()"
now=dt.datetime.now()
weekday=now.weekday()
if True:
    try:
        with open("quotes.txt") as quote:
            all_quote=quote.readlines()
            today_quote=random.choice(all_quote)
    except FileExistsError:
        pass
    finally:
        print(today_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="pupuql123@gmail.com",
            msg=f"Subject:Friday motivation \n\n 'hello everynyan..hru..faine sank you'"
        )
        connection.close()
