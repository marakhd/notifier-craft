from telebot import TeleBot
from aiogram import Bot

class Telegram(TeleBot):
    def __init__(self, token: str, parse_mode: str=None, *args, **kwargs):
        super().__init__(token=token, parse_mode=parse_mode, *args, **kwargs)
        
    # def send_message(self, chat_id, text):
    #     super().send_message(chat_id=chat_id, text=text)


class AsyncTelegram(Bot):
    def __init__(token, *args, **kwargs):
        super().__init__(token=token, *args, **kwargs)
        
    async def send_message(self, chat_id, text, parse_mode="HTML", *args, **kwargs):
        await super().send_message(chat_id=chat_id, text=text, *args, **kwargs)

