from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Кнопка 1", callback_data="btn1"),
        InlineKeyboardButton("Кнопка 2", callback_data="btn2")
    )
    return markup