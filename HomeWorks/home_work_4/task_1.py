import telebot
import credentials

token = credentials.BOT_TOKEN

bot = telebot.TeleBot(token)

my_name = "Илья"

@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)