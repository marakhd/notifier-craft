from telebot import TeleBot

class Telegram(TeleBot):
    def __init__(self, token: str, parse_mode: str=None, *args, **kwargs):
        super().__init__(token=token, parse_mode=parse_mode, *args, **kwargs)
        
    # def send_message(self, chat_id, text):
    #     super().send_message(chat_id=chat_id, text=text)
