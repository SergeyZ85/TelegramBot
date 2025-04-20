from telebot.types import ReplyKeyboardMarkup

def get_reply_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Да", "Нет")
    return markup