from telegram.ext import Dispatcher,Updater,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random


#Buttons:
larger = InlineKeyboardButton('⬆️', callback_data='⬆️')
smaller = InlineKeyboardButton('⬇️', callback_data='⬇️')

kb = InlineKeyboardMarkup([[larger,smaller]])

#Variables:
answer = ""
peopleinthegame = []

number1 = random.randint(1,6)
number2 = random.randint (1,6)
number3 = random.randint (1,6)
sumofthenumbers = number1 + number2 + number3
message = 'I have generated three numbers from 1 - 6. \n \n If you think the sum of all three numbers is 10 or above, press the ⬆️ button.\n If you think the sum of all three numbers is 10 or below, press the ⬇️ button.\n \n If you guess right, you win a prize!\n\nThe people who are playing are:\n %s ' %(peopleinthegame) 
games = {}

def sendmessage(update, context):
    global peopleinthegame
    global kb
    global message

    context.bot.send_message(chat_id=update.effective_chat.id, text= (message),reply_markup=kb)

def playgame(update, context):
    global answer

    if sumofthenumbers < 10:
        answer = "⬇️"
    else:
        answer = "⬆️"

    sendmessage(update, context)
    print (answer)
def buttonCallback(update, context):
    global answer
    global sumofthenumbers
    global message
    query = update.callback_query

    first_name = update.effective_user.first_name

    if not first_name in peopleinthegame:
        peopleinthegame.append(first_name)

    if sumofthenumbers < 10:
        answer = "⬇️"
    else:
        answer = "⬆️"

    if query.data == answer:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You got it correct!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You got it wrong!")

def add_playgamehandler(dp:Dispatcher):
    playgame_handler = CommandHandler('playgame', playgame)
    dp.add_handler(playgame_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback))