import random
from telegram.ext import CommandHandler,Dispatcher


def TakeAwayEXP(BotUpdate, context):
    Possibilitys = [
    "haha! you lost 1000 EXP!",
    "So lucky... You don't lose EXP...",
    "You just lose 500 EXP, as normal.",
    "THE GODS WILL DECIDE YOUR FATE, AND THEY HAVE DECIDED TO TAKE AWAY %s EXP" %(random.randint(500, 1500))]
    #print (Possibilitys)
    TakeAwayEXPmessage = Possibilitys[random.randint(0, 3)]    
    context.bot.send_message(chat_id=BotUpdate.effective_chat.id, text = TakeAwayEXPmessage + " - By Parker")

def addHandler(dp:Dispatcher):
    TakeAwayEXP_handler = CommandHandler('TakeAwayEXP', TakeAwayEXP)
    dp.add_handler(TakeAwayEXP_handler)