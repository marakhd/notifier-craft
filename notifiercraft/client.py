from telebot import TeleBot
from .sender import Telegram, Email
from .error import UnsupportedSenderType

class CreateClient:
    notify = {
        "telegram": [],
        "email": [],
        # "discord": [],
        # "sms": [],
        # "vk": []
    }
    
    def __init__(self, *senders) -> None:
        self.senders_types(senders)
        
    def senders_types(self, senders):
        for sender in senders:
            if isinstance(sender, Telegram):
                self.notify["telegram"].append(sender)
            elif isinstance(sender, Email):
                self.notify["email"].append(sender)
            else:
                raise UnsupportedSenderType
    
    class send:
        def telegram(self, chat_id, text):
            for tg in self.notify["telegram"]:
                tg.send_message(chat_id=chat_id, text=text)
                
        def email(self, email, text):
            for email in self.notify["email"]:
                email.send_message(email=email, text=text)
                
        

