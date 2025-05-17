import telebot

bot = telebot.TeleBot("7961277636:AAEg5Pj7GGCC1snfiEt3sOAyMaUewtcwRQw")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello, I'm alive on Fly.io!")

bot.polling()
