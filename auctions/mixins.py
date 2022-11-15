from django.conf import settings
from twilio.rest import Client
import random

class Messahandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp


    def send_otp_on_phone(self):
        client = Client('AC16a0e04dcee111f6d60177f94ea7d0ab','412836f9276a34915919b1585e10ed43')
        message = client.messages.create(
            body=f'Your otp is {self.otp}',
            from_='+17262275861',
            to=self.phone_number
        )
        print(message.sid)
        return message.sid
