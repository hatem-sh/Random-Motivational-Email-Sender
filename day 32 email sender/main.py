import smtplib
import datetime as dt
import random

my_email = "**************"
password = "***********"


with open("quotes.txt") as file:
    lines = []
    for line in file:
        lines.append(line)
random_motivation = random.choice(lines)

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
print(now)
if day_of_week == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="hatemshohof@gmail.com",
                            msg=f"Subject:random_motivation \n\n{random_motivation}")
