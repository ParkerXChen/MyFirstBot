from icalevents.icalevents import events
from datetime import date, timedelta, time
from telegram.ext import Dispatcher, CallbackContext, CommandHandler
import pytz
import coins

def setcal(update,context):
    list_of_timezones = pytz.all_timezones
    coins.check_user(update.message.from_user.id)
    if not len(context.args) == 2:
        update.message.reply_text('Sorry, but you need to follow the following format:\n\n/setcal(timezone)(url)')
    else:
        if context.args[0] in list_of_timezones:
            coins.set_timezone(update.message.from_user.id,context.args[0])
            coins.set_url(update.message.from_user.id,context.args[1])
            update.message.reply_text(f'OK! Your timezone has been set to {context.args[0]}, and your calander URL has been set to {context.args[1]}.')
        else:
            update.message.reply_text(f'Sorry, that is not a valid timezone. Check all of the valid timezones here:\n\nhttps://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568')

def add_geteventshandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('setcal', setcal)) 