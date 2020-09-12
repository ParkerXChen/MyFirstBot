import random
from telegram.ext import CommandHandler,Dispatcher


def addEXP (BotUpdate, context):
    Possibilitys = [
    "haha! you don't get EXP!",
    "You get %s EXP!" %(random.randint(1,100))]
    #print (Possibilitys)
    addEXPmessage = Possibilitys[random.randint(0, 1)]    
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text = addEXPmessage + " - By Parker")

def addHandler(dp:Dispatcher):
    addEXP_handler = CommandHandler('addEXP', addEXP)
    dp.add_handler(addEXP_handler)