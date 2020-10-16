from telegram.ext import Dispatcher,Updater,CommandHandler
import random

games = {}

def showhelp():
    return """
    You guessed a number from 0 - 100.
/guessnumber Check your current status and get help.
/guessnumber followed by a number 1-100 to guess that number.
    """

def guessnumber(update, context):
    global games
    chatid = update.message.chat.id
    
    if not (chatid) in games:
        games[chatid] = {'botsnumber':random.randint(1,99), "member":{}}
    print (games)
    
    if not update.message.from_user.id in games[chatid]:
        games[chatid][update.message.from_user.id] = 0
    if len(context.args) == 0:
        update.message.reply_text(showhelp())
    else:
        if (context.args[0]).isdigit():
            number = int(context.args[0])
            games[chatid][update.message.from_user.id] += 1
            if number == games[chatid]['botsnumber']:
                update.message.reply_text("You guessed my number! It only took you %s tries!" %(games[chatid][update.message.from_user.id]))
            elif number < games[chatid]['botsnumber']: 
                update.message.reply_text("Nope! Too small! Try again!  Number of tries: %s" %(games[chatid][update.message.from_user.id]))
            else:
                update.message.reply_text("Nope! Too big! Try again! Number of tries: %s" %(games[chatid][update.message.from_user.id]))
        else: update.message.reply_text("Is that even a number?")


def reset(update, context):
    global games
    chatid = update.message.chat.id     
    games[chatid].clear()
    games[chatid]['botsnumber'] = random.randint (1,99)
    update.message.reply_text("RESET COMPLETE")

def add_guesshandler(dp:Dispatcher):
    guessnumber_handler = CommandHandler('guessnumber', guessnumber)
    dp.add_handler(guessnumber_handler)

def add_resethandler(dp:Dispatcher):
    reset_handler = CommandHandler('reset', reset)
    dp.add_handler(reset_handler)