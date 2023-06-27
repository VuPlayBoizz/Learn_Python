#import smtplib

#my_email = "hoahoc866@gmail.com"
#password = "stdjcbggwfkxxtcn"

#with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #connection.starttls()
    #connection.login(user=my_email, password=password)
    #connection.sendmail(
        #from_addr=my_email,
        #to_addrs="nguyenbavu1902@gmail.com",
        #msg="Subject: Hello\n\nThis is the body of my email."
    #)
#import datetime

#now = datetime.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(now)

#date_of_birth = datetime.datetime(year= 2002, month= 2, day= 15)
#print(date_of_birth)


import smtplib
import datetime
import random

my_email = "hoahoc866@gmail.com"
password = "stdjcbggwfkxxtcn"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    #print(quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nguyenbavu1902@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )