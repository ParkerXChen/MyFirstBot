from telegram.ext import Dispatcher,Updater,CommandHandler
import random
botsnumber = random.randint (1,100)
NumberOfGuessesDic = {
    
}

def showhelp():
    return """
    You guessed a number from 0 - 100.
/guessnumber Check your current status and get help.
/guessnumber followed by a number 1-100 to guess that number.
    """

def guessnumber(update, context):
    global botsnumber
    global NumberOfGuessesDic
    
    if not update.message.from_user.id in NumberOfGuessesDic:
        NumberOfGuessesDic[update.message.from_user.id] = 0

    if len(context.args) == 0:
        update.message.reply_text(showhelp())
    else:
        if (context.args[0]).isdigit():
            print (botsnumber)
            number = int(context.args[0])
            NumberOfGuessesDic[update.message.from_user.id] += 1
            if number == botsnumber:
                update.message.reply_text("You guessed my number! It only took you %s tries!" %(NumberOfGuessesDic[update.message.from_user.id]))
            elif number < botsnumber: 
                update.message.reply_text("Nope! Too small! Try again!  Number of tries: %s" %(NumberOfGuessesDic[update.message.from_user.id]))
            else:
                update.message.reply_text("Nope! Too big! Try again! Number of tries: %s" %(NumberOfGuessesDic[update.message.from_user.id]))
        else: update.message.reply_text("Is that even a number?")


def reset(update, context):
    global botsnumber
    global NumberOfGuessesDic
    botsnumber = random.randint (1,100)
    NumberOfGuessesDic.clear()
    update.message.reply_text("RESET COMPLETE")
    print (botsnumber)

def add_handler(dp:Dispatcher):
    guessnumber_handler = CommandHandler('guessnumber', guessnumber)
    dp.add_handler(guessnumber_handler)

def add_handler2(dp:Dispatcher):
    reset_handler = CommandHandler('reset', reset)
    dp.add_handler(reset_handler)