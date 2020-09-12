from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os

def start(BotUpdate, context):
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="I'm a bot, please talk to me!")

def eatCheese(BotUpdate, context):
    
    piecesOfCheeseLeft = 10
    cheeseMessage = "You ate a piece of cheese! you used to have %s pieces of cheese, but after eating a piece you only have %s pieces." %(
    piecesOfCheeseLeft,
    piecesOfCheeseLeft-1
    )   
    if piecesOfCheeseLeft == 0:
        print("You have no cheese left. :(")
    else:
        context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text = cheeseMessage)
        piecesOfCheeseLeft -= 1

def echo(BotUpdate, context):
    msg = " We are in a %s chat. %s said %s ，your username is %s, your uid is %s，your system is in %s" %(
        BotUpdate.message.chat.type,
        BotUpdate.message.from_user.first_name,
        BotUpdate.message.text,
        BotUpdate.message.chat.username,
        BotUpdate.message.from_user.id,
        BotUpdate.message.from_user.language_code)
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text= msg)

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

#print (TOKEN)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

eatCheese_handler = CommandHandler('eatCheese', eatCheese)
dispatcher.add_handler(eatCheese_handler)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()