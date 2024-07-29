from telebot import TeleBot
from aiogram import Bot
from asyncio import get_event_loop


class Telegram(TeleBot):
    def __init__(self, token: str, parse_mode: str=None, *args, **kwargs):
        super().__init__(token=token, parse_mode=parse_mode, *args, **kwargs)
        
    def send_message(self, chat_id, text, parse_mode="HTML", *args, **kwargs):
        super().send_message(chat_id=chat_id, text=text, parse_mode=parse_mode, *args, **kwargs)


class AsyncTelegram(Bot):
    def __init__(self, token, **kwargs):
        super().__init__(token=token, **kwargs)
        
    async def send_message(self, chat_id, text, parse_mode="HTML", *args, **kwargs):
        await super().send_message(chat_id=chat_id, text=text, parse_mode=parse_mode, *args, **kwargs)
        
    async def close(self):
        await self.session.close()

