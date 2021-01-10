from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import pafy
def ytmusic(update,context):
    if not len(context.args) == 0:
        url = context.args[0]
        video = pafy.new(url)
    else:
        video = 'Please add a URL after the command.'
    update.message.reply_text(str(video)[:-1])
    bestaudio = video.getbestaudio(preftype="m4a")
    bestaudio.download(f'/tmp{bestaudio.title}.{bestaudio.extension}')
    print(bestaudio.url)

def add_ytmusichandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('YTmusic', ytmusic))