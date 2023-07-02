import smtplib
import datetime as dt
import random
import pandas


# Email details, app password (set it up on gmail for example)
MY_EMAIL = ""
MY_PASSWORD = ""

current_day = dt.datetime.now()
today = (current_day.month, current_day.day)

# Set up your own birthdays.csv file following the example
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_number = random.randint(1, 3)

    # Opening random letter from templates folder
    file_path = f"letter_templates/letter_{letter_number}.txt"

    # Changing the name of the recipient
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Sending email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
