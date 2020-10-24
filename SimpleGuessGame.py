from telegram.ext import Dispatcher,Updater,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random

listofpeople = ""
answer = ""

#Buttons:
larger = InlineKeyboardButton('⬆️', callback_data='⬆️')
smaller = InlineKeyboardButton('⬇️', callback_data='⬇️')
join = InlineKeyboardButton('Join', callback_data='Join')

kb = InlineKeyboardMarkup([[larger,smaller,join]])

def playgame(update, context):
    global listofpeople
    global answer
    #print (update)
    firstname = update.message.from_user.first_name
    peopleinthegame = []
    
    number1 = random.randint(1,6)
    number2 = random.randint (1,6)
    number3 = random.randint (1,6)

    sumofthenumbers = number1 + number2 + number3

    if sumofthenumbers < 10:
        answer = "smaller"
    else:
        answer = "bigger"
    
    if not firstname in peopleinthegame:
        peopleinthegame.append(firstname)

    for x in peopleinthegame:
        listofpeople = listofpeople + str(x) + "\n    "
        print (listofpeople)
    update.message.reply_text ("""
    I have generated three numbers from 1 - 6.
    To join the game, press the Join button.
    After you have joined the game, guess if the sum of the three numbers I have generated is above 10 or below 10.

    If you think it is 10 or above, press the ⬆️ button.
    If you think it is below 10, press the ⬇️ button.

    If you guess right, you win a prize!

    The players are:
    %s
    """%(listofpeople) ,reply_markup=kb)

def buttonCallback(update, context):
    query = update.callback_query
    query.answer("%s Pressed %s"%(update.effective_user.first_name,query.data))


def add_playgamehandler(dp:Dispatcher):
    playgame_handler = CommandHandler('playgame', playgame)
    dp.add_handler(playgame_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback))