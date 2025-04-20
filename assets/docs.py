from telegram.ext import Application
from config.settings import BOT_TOKEN
from handlers import commands, messages, callbacks


async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(commands.start_handler)
    app.add_handler(messages.text_handler)
    app.add_handler(callbacks.button_handler)

    await app.run_polling()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())