from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import random

PiecesOfCheese = 10


def start(BotUpdate, context):
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="Hello, I am Gu3ssingBot. type /GuessNumber to guess a number.")

def guessNumber(BotUpdate, context):
    TheNumberThatImThinkingOf = random.randint(1,100)
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="Hello, I am Gu3ssingBot. I am thinking of a number from 1-100. type /GuessNumber to try and guess it.")


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

guessNumber_handler = CommandHandler('guessnumber', guessNumber)
dispatcher.add_handler(guessNumber_handler)


updater.start_polling()