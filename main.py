import telebot
from config.settings import Config
from handlers import register_handlers

bot = telebot.TeleBot(Config.BOT_TOKEN)

# Регистрируем все обработчики
register_handlers(bot)

if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()