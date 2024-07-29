from .sender import Telegram, AsyncTelegram, Email, AsyncEmail
from .error import UnsupportedSenderType
# TODO: logging

class CreateClient:
    _notify = {
        "telegram": [],
        "email": [],
        # "telegram-user": [],
        # "discord": [],
        # "vk": [],
        # "sms": [],
    }
    
    def __init__(self, *senders, ) -> None:
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

    def all(self, chat_id: int | str, email: str, text: str, subject_email) -> None:
        self.telegram(chat_id=chat_id, text=text)
        self.email(email=email, text=text, subject=subject_email)

    def telegram(self, chat_id: int | str, text: str) -> None:
        for tg in self.__notify["telegram"]:
            tg.send_message(chat_id=chat_id, text=text)

    def email(self, email: str, text: str, subject) -> None:
        for mail in self.__notify["email"]:
            mail.send_message(email=email, text=text, subject=subject)


