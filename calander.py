from telegram.ext import Dispatcher,CommandHandler
from icalevents.icalevents import events
from json import dumps
import datetime

def getevents(update,context):
    url = "webcal://p60-caldav.icloud.com/published/2/MTMwMjQzNDk4NDEzMDI0M3sQtDCMMqfWL7VMca-urO1PHNC7k1S3xOJlT4pbFvB2zTOKsoMYKAaoX8kwofUBGi0yjak_7FqpXGZUZh5MhGY"
    start = datetime.date.today() + datetime.timedelta(days=1)
    end = datetime.date.today() + datetime.timedelta(days=1)
    evs = events(url=url, start=start, end=end,fix_apple=True)
    msg = ''
    for i in evs:
        msg += f'Event: {i.summary}\nStart date / time: {str(i.start)[0:10]} / {str(i.start)[0:-8]}\n\n'
    update.message.reply_text(msg)

def add_geteventshandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('getevents', getevents))