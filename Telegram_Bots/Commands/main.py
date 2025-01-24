import telebot # You need to download module telebot. Write in console "pip install telebot" or "pip3 install telebot"
token = "" #Telegram bot token. You can create and get a token in bot "BotFather"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start']) #you need to send to your bot command "/start"
def response(msg):
    bot.send_message(msg.chat.id, "Hello, try to send me /hello")
@bot.message_handler(commands=['hello']) #you need to send to your bot command "/hello"
def response(msg):
    bot.send_message(msg.chat.id, "Hello, world!")
bot.infinity_polling()
