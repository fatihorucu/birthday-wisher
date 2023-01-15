import pandas as pd
import datetime as dt
import random
from os import listdir  # returns a list of file names in chosen directory
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("birthdays.csv")
data_records = data.to_dict(orient="records")
now = dt.datetime.now()
for item in data_records:
    if item["year"] == now.year and item["month"] == now.month and item["day"] == now.day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_name = random.choice(listdir("./letter_templates"))
        with open(f"./letter_templates/{letter_name}") as letter_file:
            letter = letter_file.read()
            new_letter = letter.replace("[NAME]", item["name"])
            print(new_letter)
# 4. Send the letter generated in step 3 to that person's email address.
            my_email = "MY_EMAIL"
            password = "PW"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()   # For Security -- Transfer Layer Security(TLS)
                connection.login(my_email, password)
                connection.sendmail(from_addr=my_email, to_addrs=item["email"], msg=f"Hey!\n\n{new_letter}")



