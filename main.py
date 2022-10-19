import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from pytz import timezone

import datetime as dt
import avatar_downloader as AD
import description_downloader as DD

token = "5434133255:AAGjeXWpvd4vtyUKKZmNLULdyMWzbNDp_l0"
bot = telegram.Bot(token=token)
#pic = "./avatar.jpg"

updater = Updater(token,
                  use_context=True)

j = updater.job_queue

my_tz = timezone('Etc/GMT-7')
send_time = dt.time(20, 42, 0, 000000, tzinfo=my_tz)

users_id = set()

def id_list_debug():
    print("current id list: " )
    print(users_id)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет, сладкий. Мои девочки самые горячие, а свое ОСОБОЕ предложение ты увидишь сразу после планерки")
    users_id.add(update.message.chat_id)
    id_list_debug()

def stop(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Для тебя показ приостановлен. Пиши /start, когда одумаешься.ы")
    if users_id:
        users_id.remove(update.message.chat_id)
    id_list_debug()

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Новая девочка появляется каждый день ровно в 11:15 \n Если хочешь отдохнуть от девочек, пиши в чат /stop")

def daily_show_slut(context: CallbackContext):
    print("SHOW")
    avatar_file = "./" + AD.Download()
    description = DD.Download()
    for id in users_id:
        context.bot.send_message(chat_id=id, text="Вот наша девочка дня")
        context.bot.send_photo(id, open(avatar_file,'rb'))
        context.bot.send_message(chat_id=id, text=description)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('help', help))

# Filters out unknown messages and commands
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  

updater.start_polling()
j.run_daily(daily_show_slut, send_time, days=(0, 1, 2, 3, 4))