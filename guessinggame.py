from telegram.ext import Dispatcher,Updater,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random

answer = ""
larger = InlineKeyboardButton('⬆️', callback_data='⬆️')
smaller = InlineKeyboardButton('⬇️', callback_data='⬇️')

kb = InlineKeyboardMarkup([[larger,smaller]])

def playgame(update, context):
    global answer

    number1 = random.randint(1,6)
    number2 = random.randint (1,6)
    number3 = random.randint (1,6)

    sumofthenumbers = number1 + number2 + number3

    if sumofthenumbers < 10:
        answer = "⬇️"
    else:
        answer = "⬆️"
    
    print (sumofthenumbers)
    update.message.reply_text ("""
    I have generated three numbers from 1 - 6.
    
    If you think it is 10 or above, press the ⬆️ button.
    If you think it is below 10, press the ⬇️ button.

    If you guess right, you win a prize!
    """ ,reply_markup=kb)

def buttonCallback(update, context):
    global answer

    query = update.callback_query
    print (query)
    if query.data == answer:
        print ("You got it correct!")
    else:
        print ("You got it wrong!")
def add_playgamehandler(dp:Dispatcher):
    playgame_handler = CommandHandler('playgame', playgame)
    dp.add_handler(playgame_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback))