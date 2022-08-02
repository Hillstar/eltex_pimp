from time import sleep
import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import avatar_downloader as AD
import description_downloader as DD

token = "5434133255:AAGjeXWpvd4vtyUKKZmNLULdyMWzbNDp_l0"
bot = telegram.Bot(token=token)
pic = "./avatar.jpg"

updater = Updater(token,
                  use_context=True)
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет, сладкий. Мои девочки самые горячие, и специально для тебя у меня есть особое предложение")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Если хочешь увидеть прошмандовку дня, пиши '/show' в чат")

def show_slut(update: Update, context: CallbackContext):
    avatar_file = "./" + AD.Download()
    description = DD.Download()
    chat_id = update.message.chat_id
    update.message.reply_text("Вот наша девочка дня")
    bot.send_photo(chat_id, open(avatar_file,'rb'))
    update.message.reply_text(description)
    #update.message.reply_text("Следующую девочку можно увидеть через час")

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('show', show_slut))
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
# Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  

updater.start_polling()