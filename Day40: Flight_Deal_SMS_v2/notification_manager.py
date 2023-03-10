from twilio.rest import Client
import smtplib
import os

TWILIO_SID = os.environ['SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = os.environ['MY_NUM']
TWILIO_VERIFIED_NUMBER = os.environ['MY_VER_NUM']
my_email = os.environ['EMAIL']
password = os.environ['EMAIL_PW']

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, send_msg, email_list):
        for email in email_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=send_msg
                )
