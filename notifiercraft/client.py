from .sender import Telegram, Email
from .error import UnsupportedSenderType

class CreateClient:
    notify = {
        "telegram": [],
        "email": [],
        # "telegram-user": [],
        # "discord": [],
        # "vk": []
        # "sms": [],
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
            
    @property
    def send(self):
        return Send(self)


class Send:
    def __init__(self, client) -> None:
        self.notify = client.notify

    def all(self, text):
        for tg in self.notify["telegram"]:
            tg.send_message(text=text)
        for email in self.notify["email"]:
            email.send_message(text=text)

    def telegram(self, chat_id, text):
        for tg in self.notify["telegram"]:
            tg.send_message(chat_id=chat_id, text=text)

    def email(self, email, text):
        for email in self.notify["email"]:
            email.send_message(email=email, text=text)


