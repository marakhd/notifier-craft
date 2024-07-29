from typing import Union

from .sender import Telegram, AsyncTelegram, Email, AsyncEmail
from .error import UnsupportedSenderType

class CreateClient:
    _notify: dict[str, Union[list[Telegram | AsyncTelegram], list[Email | AsyncEmail]]] = {
        "telegram": [],
        "email": [],
        # "telegram-user": [],
        # "discord": [],
        # "vk": []
        # "sms": [],
    }
    
    def __init__(self, *senders) -> None:
        self.__senders_types(senders)
        
    def __senders_types(self, senders):
        for sender in senders:
            if isinstance(sender, Telegram):
                self._notify["telegram"].append(sender)
            elif isinstance(sender, Email):
                self._notify["email"].append(sender)
            else:
                raise UnsupportedSenderType
            
    @property
    def send(self):
        return Send(self)


class Send:
    def __init__(self, client: CreateClient) -> None:
        self.__notify = client._notify

    def all(self, text):
        for tg in self.__notify["telegram"]:
            tg.send_message(text=text)
        for email in self.__notify["email"]:
            email.send_message(text=text)

    def telegram(self, chat_id, text):
        for tg in self.__notify["telegram"]:
            tg.send_message(chat_id=chat_id, text=text)

    def email(self, email, text):
        for email in self.__notify["email"]:
            email.send_message(email=email, text=text)


