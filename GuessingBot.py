from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Dispatcher,Updater
import os
import random

BotsNumber = random.randint (1,100)
NumberOfGuesses = 0

def reset(update, context):
    global BotsNumber
    global NumberOfGuesses
    BotsNumber = random.randint (1,100)
    NumberOfGuesses = 0
    update.message.reply_text("RESET COMPLETE")


def start(update, context):
    update.message.reply_text("HAHA WE STARTED")


def help():
    return """
    You guessed a number from 0 - 100.
/guessnumber Check your current status and get help.
/guessnumber followed by a number 1-100 to guess that number.
    """

def guessNumber(update, context):
    global BotsNumber
    global NumberOfGuesses
    if len(context.args) == 0:
        update.message.reply_text(help())
    else:
        number = int(context.args[0])
        print (number)
        print (BotsNumber)
        NumberOfGuesses += 1
        if (number) == BotsNumber:
            update.message.reply_text("You guessed my number! It only took you %s tries!" %(NumberOfGuesses))
            print (BotsNumber)
        else:
            if number < BotsNumber:
                update.message.reply_text("Nope! Too small! Try again!  Number of tries: %s" %(NumberOfGuesses))
            else:
                update.message.reply_text("Nope! Too big! Try again! Number of tries: %s" %(NumberOfGuesses))

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('GuessingBotToken')


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

reset_handler = CommandHandler('reset', reset)
dispatcher.add_handler(reset_handler)

guessNumber_handler = CommandHandler('guessnumber', guessNumber)
dispatcher.add_handler(guessNumber_handler)


updater.start_polling()
