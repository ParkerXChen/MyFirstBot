from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
from json import dumps

def getobjinfo (msgtype,msgobj):
    msg = ""
    for i in msg_type[msgtype]:
        msg += str(f'{i} = {msgobj.__dict__[i]},\n\n')
    return msg

def getmsgtype(update,context):
    global msg_type
    msg = ''
    msg_type = {
        "video":["file_id","file_unique_id","width","height","duration"],
        "photo":["file_id","file_unique_id","width","height","file_size"],
        "audio":["file_id","file_unique_id","mime_type","file_size"],
        "animation":["file_id","file_unique_id","width","height","duration"],
        "sticker":["file_id","file_unique_id","width","height","is_animated"],
        "videomsg":["file_id","file_unique_id","length","duration"],
        "voicemsg":["file_id","file_unique_id","duration","mime_type","file_size"]
    }
    if update.message.reply_to_message:
        if update.message.reply_to_message.video:
            obj = update.message.reply_to_message.video
            strobj = 'video'
        elif update.message.reply_to_message.photo:
            obj = update.message.reply_to_message.photo[2]
            strobj = 'video'
        elif update.message.reply_to_message.audio:
            obj = update.message.reply_to_message.audio
            strobj = 'video'
        elif update.message.reply_to_message.animation:
            obj = update.message.reply_to_message.animation
            strobj = 'video'
        elif update.message.reply_to_message.sticker:
            obj = update.message.reply_to_message.sticker
            strobj = 'video'
        elif update.message.reply_to_message.video_note:
            obj = update.message.reply_to_message.video_note
            strobj = 'video'
        elif update.message.reply_to_message.voice:
            obj = update.message.reply_to_message.voice
            strobj = 'video'
        msg = f'That\'s a {strobj}.\n\n{getobjinfo(strobj,obj)}'
    else:
        msg = 'Helloooooo?! This command gives you the info for the MESSAAGE YOU REPLIED TO! You didn\'t even reply to anything!'
    update.message.reply_text(msg)

def add_getmsgtypehandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('getmsgtype', getmsgtype))

def get_command():
    return [BotCommand('getmsgtype','Parker Yeet')]                                                                                                                                                                   