import telebot
import time
from flask import Flask, request
token="866320791:AAGhkMNQSh5biaZyqCT4tWeQOqcyEetYgX0"
url="http://smiksha.pythonanywhere.com/"
bot=telebot.TeleBot()
from datetime import datetime
a=['' for i in range (100)]
b=['' for i in range (100)]
@bot.message_handler(commands=["ctart"])
def send_counter(message):
    message1=bot.reply_to(message,1)
    time.sleep(1)
    for i in range(2,11):
        bot.edit_message_text(text=i,chat_id=message1.chat.id,message_id=message1.message_id)
        time.sleep(1)
    bot.delete_message(chat_id=message1.chat.id,message_id=message1.message_id)
    if a[0]:
        bot.delete_message(a[0].chat.id,a[0].message_id)
@bot.message_handler(commands=["jopa"])
def send_viabot(message):
    a[0]=bot.send_message(message.chat.id,1)
    a[0]=bot.edit_message_text(text=3,chat_id=a[0].chat.id,message_id=a[0].message_id)
    bot.delete_message(message.chat.id,message.message_id)
    print(a[0])
bot.polling(none_stop=True, interval=0)