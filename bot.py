from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import rewards
import guesscmd,coins,votecmd, pinfocmd, ainfocmd, getmsgtypecmd, youtubemusic, calander

def start(update, context):
    print(update)
    msg = "aaa"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

rewards.add_handler(dispatcher)
guesscmd.add_handler(dispatcher)
coins.add_handler(dispatcher)
votecmd.add_handler(dispatcher)
pinfocmd.add_pinfohandler(dispatcher)
ainfocmd.add_ainfohandler(dispatcher)
getmsgtypecmd.add_getmsgtypehandler(dispatcher)
youtubemusic.add_ytmusichandler(dispatcher)
calander.add_geteventshandler(dispatcher)

commands = rewards.get_command() + guesscmd.get_command() +  coins.get_command() + votecmd.get_command() + pinfocmd.get_command() + ainfocmd.get_command() + getmsgtypecmd.get_command() 
bot = updater.bot
bot.set_my_commands(commands)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()