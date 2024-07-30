from notifiercraft import CreateAsyncClient, AsyncTelegram, AsyncEmail
import asyncio

tg = AsyncTelegram(
    token="6804851619:AAElnF-gnZ5_X9rDZ6LiJvDODgQG2CURvcA"
)
email = AsyncEmail(
    host="smtp.gmail.com",
    port=587,
    login="example@gmail.com",
    passw="password"
)
client = CreateAsyncClient(
    tg,
    email
)

async def main():
    await client.send.telegram(chat_id=2075302695, text="AsyncHello1")
    await client.send.email(email="marakin09@mail.ru", text="AsyncHello1", subject="Asyncsubject")
    await client.send.all(chat_id=2075302695, email="marakin09@mail.ru", text="AsyncHello1", subject_email="Asyncsubject")
    await tg.close()
    
asyncio.run(main())
