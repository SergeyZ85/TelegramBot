from telebot.types import Message

def register_message_handlers(bot):
    dicti = {
        "sashka": "Какашка!",
        "сашка": "Какашка!",
        "кирюха": "Хуй те в ухо!",
        "kiruha": "Хуй те в ухо!",
        "mishka": "Огромная дырка!",
        "мишка": "Огромная дырка!",
        "володя": 'Долбоеб!',
        "вовка": 'От хуя головка!',
        "вован": 'Уебан!',
        "сережа": 'Крепка жопа, кривая рожа!',
        "сергей": 'Он отличный парень, несмотря на то, что гей!',
        "стас": 'Латентный пидорас!',
        "деня": 'Четкий пацан! И нож красивый...',
    }

    helpushka = "Введите имя друга."

    @bot.message_handler()
    def get_text_messages(message):
        mess = message.text.lower()
        if mess in dicti:
            bot.send_message(message.from_user.id, dicti[mess])
        elif mess in ["/start", "/help", "?"]:
            bot.send_message(message.from_user.id, helpushka)
        elif mess == "sadam":
            video = open("static/South.mp4", "rb")
            bot.send_video(message.from_user.id, video)
            bot.send_video(message.from_user.id, "FILEID")
        else:
            bot.send_message(message.from_user.id, "Хер его, че те надо")