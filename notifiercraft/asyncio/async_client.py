from ..error import UnsupportedSenderType
from ..sender import AsyncTelegram, AsyncEmail
from ..client import CreateClient

from asyncio import run

class CreateAsyncClient:
    _notify = CreateClient._notify

    def __init__(self, *senders) -> None:
        run(self.__senders_types(senders))

    def __senders_types(self, senders: tuple):
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

    async def all(self, text):
        async for tg in self.__notify["telegram"]:
            await tg.send_message(text=text)
        async for email in self.__notify["email"]:
            email.send_message(text=text)

    async def telegram(self, chat_id, text):
        async for tg in self.__notify["telegram"]:
            await tg.send_message(chat_id=chat_id, text=text)

    async def email(self, email, text):
        async for email in self.__notify["email"]:
            await email.send_message(email=email, text=text)
