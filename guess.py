from telegram.ext import Dispatcher,Updater,CommandHandler
import random

Botsnumber = random.randint (1,100)
NumberOfGuesses = 0

def guessnumber(update, context):
    global botsnumber
    global NumberOfGuesses
    if len(context.args) == 0:
        update.message.reply_text(message)
    else:
        if (context.args[0]).isdigit():
            number = int(context.args[0])
            print (number)
            print (botsnumber)
            NumberOfGuesses += 1
            if (number) == botsnumber:
                update.message.reply_text("You guessed my number! It only took you %s tries!" %(NumberOfGuesses))
                print (botsnumber)
            else:
                if number < botsnumber:
                    update.message.reply_text("Nope! Too small! Try again!  Number of tries: %s" %(NumberOfGuesses))
                else:
                    update.message.reply_text("Nope! Too big! Try again! Number of tries: %s" %(NumberOfGuesses))
        else: update.message.reply_text("Is that even a number?")

def reset(update, context):
    global botsnumber
    global NumberOfGuesses
    botsnumber = random.randint (1,100)
    NumberOfGuesses = 0
    update.message.reply_text("RESET COMPLETE")

def add_handler(dp:Dispatcher):
    guessnumber_handler = CommandHandler('guessnumber', guessnumber)
    dp.add_handler(guessnumber_handler)

def add_handler2(dp:Dispatcher):
    reset_handler = CommandHandler('reset', reset)
    dp.add_handler(reset_handler)