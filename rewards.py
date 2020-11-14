from telegram.ext import Dispatcher,CommandHandler
import random

def rewards(update, context):
    reward = random.randint (1,200)
    
    update.message.reply_text("NICE! You get %s EXP!" %(reward))

def add_handler(dp:Dispatcher):
    start_handler = CommandHandler('rewards', rewards)
    dp.add_handler(start_handler)
