from telebot.types import Message

def register_message_handlers(bot):
    @bot.message_handler(func=lambda msg: True)
    def echo_all(message: Message):
        bot.reply_to(message, message.text)