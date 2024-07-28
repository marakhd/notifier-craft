from notifiercraft import CreateClient, Telegram

tg = Telegram(
    token="6804851619:AAH4nrU8f5QJvX5R4j4pb9XSLIqr-2Tj3fI"
)
client = CreateClient(
    tg
)

client.send.telegram(chat_id=2075302695, text="Hello").email(email="test@e.e", text)
