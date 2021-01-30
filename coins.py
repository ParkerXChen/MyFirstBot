import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
import config

# {
#     chatid: {
#         uid :{
#             'name': first_name,
#             'coins': 123,
#             'count': 0,
#             'dailytime' : time
#         }
#     }
# }

coins = config.CONFIG["coins"]

def check_user(uid):
    uid = str(uid)
    if not uid in coins.keys():
        coins[uid] = {'timezone':'','calurl':''}

def set_timezone(uid,timezone):
    uid = str(uid)
    coins[uid]['timezone'] = timezone
    save()

    
def save():
    config.CONFIG["coins"] = coins
    config.save_config()

def get_command():
    return [BotCommand('coins','看看你的金币有没有丢失')]