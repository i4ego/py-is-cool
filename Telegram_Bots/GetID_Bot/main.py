import telebot # You need to download module telebot. Write in console "pip install telebot" or "pip3 install telebot"
token = "" #Telegram bot token. You can create and get a token in bot "BotFather"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start']) #if you send to your bot command "/start", he send to you "Your ID is <your id>"
def response(msg):
    bot.send_message(msg.chat.id, f"Your ID is {msg.chat.id}")
bot.infinity_polling()
