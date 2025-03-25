# Starting week motivation project
import smtplib
from datetime import *
import random

MY_EMAIL = "karimelwaraky50@gmail.com"
MY_PASSWORD = " Your app password that is generated in gmail called 'app password' "

now = datetime.now()
weekday = now.weekday()       #monday is zero

if weekday == 4:
    with open("quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Starting week motivation\n\n{quote}")

