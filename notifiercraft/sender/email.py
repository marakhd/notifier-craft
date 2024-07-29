from smtplib import SMTP
from email.mime.text import MIMEText
from asyncio import get_event_loop, to_thread


class Email(SMTP):
    def __init__(self, host: str, port: int | str, login: str, passw: str, tls: bool=True):
        super().__init__(host=host, port=int(port))
        if tls == True:
            super().starttls()
        if login and passw:
            super().login(user=login, password=passw)
        self.email = login
        
    @staticmethod
    def __validate_and_convert_email(email: str | list[str]) -> list[str]:
        if isinstance(email, str):
            return [email]
        elif isinstance(email, list) and all(isinstance(addr, str) for addr in email):
            return email
        else:
            raise TypeError("email must be a string or a list of strings")
            
    def send_message(self, email: str | list[str], subject: str, text: str):
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = email
        super().sendmail(from_addr=self.email, 
                         to_addrs=self.__validate_and_convert_email(email),
                         msg=msg.as_string())


class AsyncEmail(Email):
    def __init__(self, host, port, login, passw, tls: bool=True):
        super().__init__(host, port, login, passw, tls)

    async def send_message(self, email: str | list[str], subject: str, text: str):
        loop = get_event_loop()
        await loop.run_in_executor(None, super().send_message, email, subject, text)
