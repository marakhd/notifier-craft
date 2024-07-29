from notifiercraft import CreateClient, Telegram, Email

tg = Telegram(
    token="6804851619:AAElnF-gnZ5_X9rDZ6LiJvDODgQG2CURvcA"
)
email = Email(
    host="smtp.gmail.com",
    port=587,
    login="example@gmail.com",
    passw="passw"
)
client = CreateClient(
    tg,
    email
)

client.send.telegram(chat_id=2075302695, text="Hello1")
client.send.email(email="marakin09@mail.ru", text="Hello1", subject="subject")
client.send.all(chat_id=2075302695, email="marakin09@mail.ru", text="Hello1", subject_email="subject")