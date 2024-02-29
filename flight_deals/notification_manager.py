from twilio.rest import Client
from smtplib import SMTP
import os
from dotenv import load_dotenv
load_dotenv()


TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
# seteamos las variables de entorno para usar servicios de gmail.
PASSWORD_EMAIL = os.getenv("PASSWORD_EMAIL")


class NotificationManager:
    #  a penas creo un objeto del tipo clase NotiicationManager, se crea el cliente usando TWILIO
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Creo el metodo enviar mensaje, asi como hice con enviar mail en JS es la consulta a la API
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+16592223732",
            to="+34644053023",
        )
        # Prints if successfully sent.
        print(message.sid)
    
    def send_emails(self, emails, message):
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="nmapi2022@gmail.com", password=PASSWORD_EMAIL)
            for email in emails:
                connection.sendmail(
                    from_addr="nmapi2022@gmail.com",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )