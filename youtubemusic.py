from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
import pafy
import os
def ytmusic(update,context):
    if not len(context.args) == 0:
        url = context.args[0]
        if 'www.youtube.com' in url:
            video = pafy.new(url)
            print (video.length)
            if video.length <= 6000:
                bestaudio = video.getbestaudio(preftype="m4a")
                audiofile = f'/tmp/{bestaudio.title}.{bestaudio.extension}'
                bestaudio.download(audiofile)
                update.message.reply_audio(open(audiofile, 'rb'),caption=str(video)[:-1])
                os.remove(audiofile)
            else:
                update.message.reply_text('Sorry, but that video is too long for me to download and send to you. Please try a similar video that is shorter.')
        else:
            update.message.reply_text('Sorry, but that is not a youtube url.')
    else:
        update.message.reply_text('Sorry, but I need a URL after the command.')

def add_ytmusichandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('YTmusic', ytmusic))