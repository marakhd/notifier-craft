from ..error import UnsupportedSenderType
from ..sender import AsyncTelegram, AsyncEmail
from ..client import CreateClient

from asyncio import run

class CreateAsyncClient:
    _notify = CreateClient._notify

    def __init__(self, *senders) -> None:
        run(self.__senders_types(senders))

    async def __senders_types(self, senders: tuple):
        for sender in senders:
            if isinstance(sender, AsyncTelegram):
                self._notify["telegram"].append(sender)
            elif isinstance(sender, AsyncEmail):
                self._notify["email"].append(sender)
            else:
                raise UnsupportedSenderType
            
    @property
    def send(self):
        return AsyncSend(self)

class AsyncSend:
    def __init__(self, client: CreateAsyncClient) -> None:
        self.__notify: dict[str, list] = client._notify

    async def all(self, chat_id, email, text, subject_email):
        await self.telegram(chat_id=chat_id, text=text)
        await self.email(email=email, text=text, subject=subject_email)

    async def telegram(self, chat_id, text):
        for tg in self.__notify["telegram"]:
            await tg.send_message(chat_id=chat_id, text=text)

    async def email(self, email, text, subject):
        for mail in self.__notify["email"]:
            await mail.send_message(email=email, text=text, subject=subject)
