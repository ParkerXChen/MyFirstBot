from telegram.ext import Dispatcher,Updater,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random

bigbutton = InlineKeyboardButton('big', callback_data='big')
smallbutton = InlineKeyboardButton('small', callback_data='small')
okbutton = InlineKeyboardButton('ok', callback_data='ok')
nullbutton = InlineKeyboardButton('null', callback_data='null')

kb = InlineKeyboardMarkup([[bigbutton,smallbutton,okbutton,nullbutton]])

games = {}

def showhelp():
    return """
    You guessed a number from 0 - 100.
/guessnumber Check your current status and get help.
/guessnumber followed by a number 1-100 to guess that number.
    """

def guessnumber(update, context):
    global kb
    global games
    chatid = update.message.chat.id
    
    if not (chatid) in games:
        games[chatid] = {'botsnumber':random.randint(1,99), "member":{}}
    print (games)
    if not update.message.from_user.id in games[chatid]:
        games[chatid][update.message.from_user.id] = 0
    if len(context.args) == 0:
        update.message.reply_text(showhelp(),reply_markup=kb)
    else:
        if (context.args[0]).isdigit():
            number = int(context.args[0])
            games[chatid][update.message.from_user.id] += 1
            if number == games[chatid]['botsnumber']:
                update.message.reply_text("You guessed my number! It only took you %s tries!" %(games[chatid][update.message.from_user.id]),reply_markup=kb)
            elif number < games[chatid]['botsnumber']: 
                update.message.reply_text("Nope! Too small! Try again!  Number of tries: %s" %(games[chatid][update.message.from_user.id]),reply_markup=kb)
            else:
                update.message.reply_text("Nope! Too big! Try again! Number of tries: %s" %(games[chatid][update.message.from_user.id]),reply_markup=kb)
        else: update.message.reply_text("Is that even a number?")

def reset(update, context):
    global kb
    global games
    chatid = update.message.chat.id     
    if (chatid) in games:
        games[chatid].clear()
        games[chatid]['botsnumber'] = random.randint (1,99)
        update.message.reply_text("RESET COMPLETE")
    else:
        update.message.reply_text("Oops! No number to reset!")

def add_resethandler(dp:Dispatcher):
    reset_handler = CommandHandler('reset', reset)
    dp.add_handler(reset_handler) 

def add_guesshandler(dp:Dispatcher):
    guessnumber_handler = CommandHandler('guessnumber', guessnumber)
    dp.add_handler(guessnumber_handler)