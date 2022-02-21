import smtplib
import datetime as dt
import random
from private import *

my_email = MY_EMAIL
password = PASSWORD
now = dt.datetime.now()


# ------------------ Working with quotes Data -----------------------#

with open('quotes.txt') as f:
    quote_lines = f.readlines()


# ------------------ Sending email -----------------------#


def send_motivation():
    random_quote = random.choice(quote_lines).replace(' - ', '\n- ')

    with smtplib.SMTP_SSL(host='smtp.gmail.com') as connection:
        # connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=RECIPIENT,
            msg=f"Subject:This Monday's Quote\n\n{random_quote}"
        )


# ------------------ Checking the day -----------------------#

weekday = now.weekday()

if weekday == 0:
    send_motivation()
