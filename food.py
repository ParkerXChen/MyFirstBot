from telegram.ext import Dispatcher,Updater,CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import random

PiecesOfCheese = 10

Coins = 10

def work(BotUpdate, context):
    global Coins
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="Work Complete! You got 1 coin!")
    Coins += 1

def buycheese(BotUpdate, context):    
    global PiecesOfCheese
    global Coins
    if Coins>4:
        PiecesOfCheese += 10
        Coins -=5
        context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="You bought 10 pieces of cheese for 5 Coins! You now have %s pieces of cheese and %s coins!" %(
        PiecesOfCheese,
        Coins
        )
    )
    else:
         context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="You don't have enough coins left! say /work to earn more!")


def talk(BotUpdate, context):
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="I am working and I can run.")

def eatcheese(BotUpdate, context):
    global PiecesOfCheese
    if PiecesOfCheese > 0:
        context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="You ate cheese! You used to have %s pieces of cheese, but now you have %s pieces left!"%(
        PiecesOfCheese,
        PiecesOfCheese - 1)
        )
        PiecesOfCheese -= 1
    else:  
        context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text="You ate all of your cheese!")

def add_workhandler(dp:Dispatcher):
    work_handler = CommandHandler('work', work)
    dp.add_handler(work_handler)

def add_buycheesehandler(dp:Dispatcher):
    buycheese_handler = CommandHandler('buycheese', buycheese)
    dp.add_handler(buycheese_handler)

def add_talkhandler(dp:Dispatcher):
    talk_handler = CommandHandler('talk', talk)
    dp.add_handler(talk_handler)

def add_eatcheesehandler(dp:Dispatcher):
    eatcheese_handler = CommandHandler('eatcheese', eatcheese)
    dp.add_handler(eatcheese_handler)