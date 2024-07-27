from telebot import TeleBot

class Telegram(TeleBot):
    def __init__(self, token: str, parse_mode: str=None, *args, **kwargs):
        super().__init__(token=token, parse_mode=parse_mode, *args, **kwargs)
