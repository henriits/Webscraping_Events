import smtplib
from email.message import EmailMessage
import imghdr
import os

import email

SENDER = os.environ.get("MYMAIL")
RECEIVER = os.environ.get("MYMAIL")
PASSWORD = os.environ.get("Gmail_PASSWORD")


def send_email(message):
    email_message = EmailMessage()
    email_message["Subject"] = "Update!"
    # email_message.set_content("Hey, we just saw a new customer!")

    gmail = smtplib.SMTP("smtp.gmail.com", port=587)
    gmail.ehlo()
    gmail.starttls()

    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
