from django.conf import settings
from twilio.rest import Client
import random
from .config import acc_sid,auth_token

class Messahandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp


    def send_otp_on_phone(self):
        client = Client(acc_sid,auth_token)
        message = client.messages.create(
            body=f'Your otp is {self.otp}',
            from_='+17262275861',
            to=self.phone_number
        )
        print(message.sid)
        return message.sid
