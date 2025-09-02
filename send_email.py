import smtplib, ssl
from dotenv import load_dotenv
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # Load environment variables
    load_dotenv()

    username = os.getenv("EMAIL1")   # sender email
    password = os.getenv("PASSWORD") # app password
    receiver = os.getenv("EMAIL2")   # recipient email

    if not username or not password or not receiver:
        raise ValueError("Missing EMAIL1, EMAIL2, or PASSWORD in .env file")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
