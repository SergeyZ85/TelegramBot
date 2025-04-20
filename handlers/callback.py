from telebot.types import CallbackQuery

def register_callback_handlers(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call: CallbackQuery):
        bot.answer_callback_query(call.id, "Кнопка нажата!")