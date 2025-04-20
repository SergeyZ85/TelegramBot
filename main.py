import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.settings import Config

bot = telebot.TeleBot(Config.BOT_TOKEN)

# Главное меню
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Погода", callback_data="weather"))
    markup.add(InlineKeyboardButton("Курсы валют", callback_data="currency"))
    markup.add(InlineKeyboardButton("Помощь", callback_data="help"))
    return markup

# Меню валют
def currency_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("USD", callback_data="currency_usd"))
    markup.add(InlineKeyboardButton("EUR", callback_data="currency_eur"))
    markup.add(InlineKeyboardButton("Назад", callback_data="main_menu"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", 
                    reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    try:
        if call.data == "weather":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "Погода сегодня: солнечно, +20°C")
            
        elif call.data == "currency":
            bot.answer_callback_query(call.id)
            bot.edit_message_text("Выберите валюту:", 
                                call.message.chat.id, 
                                call.message.message_id,
                                reply_markup=currency_menu())
            
        elif call.data.startswith("currency_"):
            currency = call.data.split("_")[1]
            rate = get_currency_rate(currency)  # Ваша функция для получения курса
            bot.answer_callback_query(call.id, f"Курс {currency.upper()}: {rate}")
            
        elif call.data == "main_menu":
            bot.answer_callback_query(call.id)
            bot.edit_message_text("Главное меню:", 
                                call.message.chat.id, 
                                call.message.message_id,
                                reply_markup=main_menu())
            
        elif call.data == "help":
            bot.answer_callback_query(call.id, "Этот бот предоставляет информацию")
            
    except Exception as e:
        print(f"Error: {e}")

def get_currency_rate(currency):
    # Заглушка - реализуйте получение реального курса
    rates = {"usd": 75.5, "eur": 85.3}
    return rates.get(currency, 0)

if __name__ == "__main__":
    bot.polling(none_stop=True)