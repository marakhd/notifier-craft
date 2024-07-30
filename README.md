# Notifier Craft

**Notifier Craft** — это мощный фреймворк для Python, предназначенный для работы с уведомлениями. 
Он предоставляет как синхронные, так и асинхронные методы для отправки уведомлений через различные каналы. 
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

Чтобы отправить уведомление с помощью синхронных методов, используйте библиотеку Telebot для Telegram и smtplib для email.

#### Пример использования с Telegram (Telebot)

    from notifier_craft import TelegramNotifier

    # Создайте экземпляр TelegramNotifier с вашим токеном и ID чата
    notifier = TelegramNotifier(token='YOUR_TELEGRAM_BOT_TOKEN', chat_id='YOUR_CHAT_ID')

    # Отправьте сообщение
    notifier.send_message('Привет, это синхронное уведомление!')

#### Пример использования с Email (smtplib)

    from notifier_craft import EmailNotifier

    # Создайте экземпляр EmailNotifier с вашими настройками SMTP
    notifier = EmailNotifier(
        smtp_server='smtp.example.com',
        smtp_port=587,
        smtp_user='your_email@example.com',
        smtp_password='your_password',
        from_email='your_email@example.com'
    )

    # Отправьте email
    notifier.send_email(
        to_email='recipient@example.com',
        subject='Тема письма',
        message='Содержание письма'
    )

### Асинхронные методы

Для асинхронной отправки уведомлений используйте библиотеку aiogram для Telegram.

#### Пример использования с Telegram (aiogram)

    import asyncio
    from notifier_craft import AsyncTelegramNotifier

    async def main():
        # Создайте экземпляр AsyncTelegramNotifier с вашим токеном и ID чата
        notifier = AsyncTelegramNotifier(token='YOUR_TELEGRAM_BOT_TOKEN', chat_id='YOUR_CHAT_ID')
        
        # Отправьте сообщение
        await notifier.send_message('Привет, это асинхронное уведомление!')

    # Запустите асинхронную функцию
    asyncio.run(main())

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

Если у вас есть вопросы или предложения, не стесняйтесь обращаться к нам!
