from smtplib import SMTP
from email.mime.text import MIMEText
from asyncio import get_event_loop


class Email(SMTP):
    def __init__(self, host: str, port: int | str, login: str, passw: str, tls: bool=True):
        super().__init__(host=host, port=int(port))
        if login and passw:
            super().login(user=login, password=passw)
        if tls == True:
            super().starttls()
        self.email = login
        
    def send_message(self, email, text):
        super().sendmail(from_addr=self.email, to_addrs=email, msg=text)


class AsyncEmail(Email):
    def __init__(self, host, port, login, passw, tls: bool=True):
        super().__init__(host, port, login, passw, tls)
        self.email = login

    async def send_message(self, email, text, *args):
        loop = get_event_loop()
        await loop.run_in_executor(None, super().sendmail, self.email, email, text, *args)
