from telegram.ext import Dispatcher,Updater,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random

#Buttons:
larger = InlineKeyboardButton('⬆️', callback_data='⬆️')
smaller = InlineKeyboardButton('⬇️', callback_data='⬇️')
join = InlineKeyboardButton('Join', callback_data='Join')

kb = InlineKeyboardMarkup([[larger,smaller,join]])

def playgame(update, context):
    firstname = update.message.chat.first_name
    peopleinthegame = []
    # query = update.callback_query
    
    if not firstname in peopleinthegame:
        peopleinthegame.append(firstname)
    print (peopleinthegame)

    update.message.reply_text('''
    Press the Join button to join the game!
    
    The people already in the game are:
    %s
     '''%(peopleinthegame),reply_markup=kb)

def buttonCallback(update, context):
    query = update.callback_query
    query.answer("%s Pressed %s"%(update.effective_user.first_name,query.data))


def add_playgamehandler(dp:Dispatcher):
    playgame_handler = CommandHandler('playgame', playgame)
    dp.add_handler(playgame_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback))