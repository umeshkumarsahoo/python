# import smtplib
# my_mail="test_umesh123@yahoo.com"
# password="RX2E6#C'G}5%Aw9"
# to="sahooumesh2003@gmail.com"
# subj="testing"
# message_text="hi bro wassup"
# try :
#     server = smtplib.SMTP("smtp.mail.yahoo.com",587)
#     server.login(user=my_mail,password=password)
#     server.sendmail(from_addr=my_mail,to_addrs=to,msg=message_text)
#     print ('ok the email has sent ')
# except:
#     print ('can\'t send the Email')
# finally:
#     server.close()
import datetime as dt
now=dt.datetime.now()
year=now.year
month=now.month
day=now.day
print(f"date is: {day}/{month}/{year}")
