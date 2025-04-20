from telebot.types import Message

def register_commands(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message: Message):
        bot.reply_to(message, "Привет! Я твой бот.")