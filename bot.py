import config
import telebot
import get_info, get_info_month, get_info_year
from datetime import datetime
from threading import Thread
import time

bot = telebot.TeleBot(config.token)
chatid = config.chatid


@bot.message_handler(commands=['info'])
def infolist(message): 
    bot.send_message(chatid, get_info.res())

@bot.message_handler(commands=['info_month'])
def infolist(message): 
    bot.send_message(chatid, get_info_month.res())

@bot.message_handler(commands=['info_year'])
def infolist(message): 
    bot.send_message(chatid, get_info_year.res())

def timecheck():
    while True:
        current = datetime.now()
        if current.hour == 22 and (10 <= current.minute <= 50):
            bot.send_message(chatid, get_info.res())
            time.sleep(72000)
        time.sleep(120)

print('bot started')
thread = Thread(target = timecheck)
thread.start()

if __name__ == '__main__':
    print('infinity polling')
    bot.infinity_polling()
