# Notifier Craft

**Notifier Craft** — это мощная библиотека для Python, предназначенный для работы с уведомлениями. 
Она предоставляет как синхронные, так и асинхронные методы для отправки уведомлений через различные каналы. 
На данный момент поддерживаются уведомления через Telegram-ботов (как синхронно с помощью Telebot, так и асинхронно с помощью aiogram) и через электронную почту (с использованием smtplib). 
В будущем планируется добавить поддержку Telegram userbot, Discord-ботов, VK-ботов, а также рассылку SMS.

## Установка

- Установка, используя пакетный менеджер pip

```bash
pip install notifier-craft
```
- Установка с GitHub

```bash
pip install git+https://github.com/marakhd/notifier-craft
```

## Использование

### Синхронные методы

Пример для иcпользования с синхронными методами

```python
from notifiercraft import CreateClient, Telegram, Email # Импортируем Client и Senders

tg = Telegram(
    token="6804851619:AAElnF-gnZ5_X9rDZ6LiJvDODgQG2CURvcA"
)

# Любой sender имеет метод send_message для отправки без создания клиента, клиент нужен для удобного управления
# tg.send_message(chat_id=0123456,
#     text="test",
#     parse_mode = "HTML",)

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

client.send.telegram(chat_id=2075302695, text="Hello1") # Отправка через Email
client.send.email(email="marakin09@mail.ru", text="Hello1", subject="subject") # Отправка через Telegram
client.send.all(chat_id=2075302695, email="marakin09@mail.ru", text="Hello1", subject_email="subject") # Отправка всеми способами
```

### Асинхронные методы

Пример для иcпользования с асинхронными методами

```python
from notifiercraft import CreateAsyncClient, AsyncTelegram, AsyncEmail # Импортируем AsyncClient и AsyncSenders
import asyncio

tg = AsyncTelegram(
    token="6804851619:AAElnF-gnZ5_X9rDZ6LiJvDODgQG2CURvcA"
)

# Любой sender имеет метод send_message для отправки без создания клиента, клиент нужен для удобного управления
# await tg.send_message(chat_id=0123456,
#     text="test",
#     parse_mode = "HTML",)


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
    await client.send.telegram(chat_id=2075302695, text="AsyncHello1") # Отправка через Email
    await client.send.email(email="marakin09@mail.ru", text="AsyncHello1", subject="Asyncsubject") # Отправка через Telegram
    await client.send.all(chat_id=2075302695, email="marakin09@mail.ru", text="AsyncHello1", subject_email="Asyncsubject") # Отправка всеми способами
    await tg.close() # Закрываем сессию
    
asyncio.run(main())
```


## Планируемые обновления

В ближайших обновлениях планируется добавление следующих возможностей:

- Поддержка Telegram userbot
- Интеграция с Discord-ботами
- Поддержка VK-ботов
- Отправка SMS

## Лицензия

Этот проект распространяется под лицензией MIT License. См. [LICENSE](LICENSE) для подробностей.

## Контрибьюции

Если вы хотите внести изменения или улучшения в проект, пожалуйста, создайте Pull Request или откройте Issue в репозитории.

---

