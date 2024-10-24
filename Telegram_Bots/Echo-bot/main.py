import telebot # You need to download module telebot. Write in console "pip install telebot" or "pip3 install telebot"
token = "" #Telegram bot token. You can create and get a token in bot "BotFather"
bot = telebot.TeleBot(token)
@bot.message_handler(content_types='text')
def response(msg):
    bot.send_message(msg.chat.id, msg.text)
    print(f"{msg.chat.id}: {msg.text}")
bot.infinity_polling()
