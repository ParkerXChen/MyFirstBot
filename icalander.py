from icalevents.icalevents import events
from datetime import date, timedelta, time
from telegram.ext import Dispatcher, CallbackContext, CommandHandler
import pytz
import coins

def timer_callback(context:CallbackContext):
    url = 'webcal://p60-caldav.icloud.com/published/2/MTMwMjQzNDk4NDEzMDI0M3sQtDCMMqfWL7VMca-urO1PHNC7k1S3xOJlT4pbFvB2zTOKsoMYKAaoX8kwofUBGi0yjak_7FqpXGZUZh5MhGY'
    tommorow = date.today() + timedelta(days=1)
    msg = ''
    es = events(url,fix_apple=True,start=tommorow,end=tommorow)
    for i in es:
        msg += f'{i.summary}\nStart: {i.start}\nEnd:{i.end}\n{i.description}\n\n'
    context.bot.send_message(chat_id=context.job.context,text=msg)

def getevents(update,context):
    chatid = update.message.chat_id
    context.job_queue.run_repeating(timer_callback,5,context=chatid)

def run_repeating(job_queue):
    chatid = -1001366387264
    job_queue.run_daily(timer_callback,
                            time(hour=11, minute=53, tzinfo=pytz.timezone('US/Eastern')),
                            days=(0, 1, 2, 3, 4, 5, 6), context=chatid)

def add_geteventshandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('getevents', getevents)) 