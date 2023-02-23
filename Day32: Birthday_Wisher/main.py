import pandas
import random
import datetime as dt
import smtplib

today = dt.datetime.now()
day = today.day
month = today.month
my_email = "mjb.python@gmail.com"
password = ""
letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

df = pandas.read_csv("birthdays.csv")
new_df = df.iterrows()
dict_thing = {(row.month, row.day):row for index, row in new_df}

for key in dict_thing:
    if key == (month, day):
        chosen_letter = random.choice(letters)
        with open(f"{chosen_letter}", "r") as file:
            data = file.read()
            data = data.replace("[NAME]", dict_thing[key]['name'])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=dict_thing[key]['email'],
                    msg=f"Subject:Birthday Wishes\n\n{data}"
                )


