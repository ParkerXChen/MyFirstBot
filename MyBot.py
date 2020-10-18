from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Dispatcher,Updater
import os
import guess
import food

def start(update, context):
    update.message.reply_text("HAHA WE STARTED")

def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN=read_file_as_str('GuessingBotToken')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

guess.add_guesshandler(dispatcher)

guess.add_resethandler(dispatcher)

food.add_workhandler(dispatcher)

food.add_talkhandler(dispatcher)

food.add_eatcheesehandler(dispatcher)

food.add_buycheesehandler(dispatcher)
updater.start_polling()