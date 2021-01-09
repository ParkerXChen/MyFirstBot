from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
from json import dumps

def getmsgtype(update,context):
    msg = ''
    msg_type = {
        "video":["file_id","file_unique_id","width","height","duration"],
        "photo":["file_id","file_unique_id","width","height","file_size"],
        "audio":["file_id","file_unique_id","width","height","file_size"],
        "animation":["file_id","file_unique_id","width","height","duration"],
        "sticker":["file_id","file_unique_id","width","height","is_animated"],
        "videomsg":["file_id","file_unique_id","length","duration"],
        "voicemsg":["file_id","file_unique_id","duration","mime_type","file_size"]
    }

    if update.message.reply_to_message:
        if update.message.reply_to_message.video:
            video = update.message.reply_to_message.video
            msg = 'That\'s a video.\n\n'
            for i in msg_type['video']:
                msg += str(f'{i} = {video.__dict__[i]},\n\n')
        elif update.message.reply_to_message.photo:
            photo = update.message.reply_to_message.photo[2]
            msg = 'That\'s a photo.\n\n'
            for i in msg_type['photo']:
                msg += str(f'{i} = {photo.__dict__[i]},\n\n')
        elif update.message.reply_to_message.audio:
            audio = update.message.reply_to_message.audio
            msg = 'That\'s an audio message.\n\n'
            for i in msg_type['audio']:
                msg += str(f'{i} = {audio.__dict__[i]},\n\n')
        elif update.message.reply_to_message.animation:
            animation = update.message.reply_to_message.animation
            msg = 'That\'s an animation.\n\n'
            for i in msg_type['animation']:
                msg += str(f'{i} = {animation.__dict__[i]},\n\n')
        elif update.message.reply_to_message.sticker:
            sticker = update.message.reply_to_message.sticker
            msg = 'That\'s a sticker.\n\n'
            for i in msg_type['sticker']:
                msg += str(f'{i} = {sticker.__dict__[i]},\n\n')
        elif update.message.reply_to_message.video_note:
            videomsg = update.message.reply_to_message.video_note
            msg = 'That\'s a video note.\n\n'
            for i in msg_type['videomsg']:
                msg += str(f'{i} = {videomsg.__dict__[i]},\n\n')
        elif update.message.reply_to_message.voice:
            voicemsg = update.message.reply_to_message.voice
            msg = 'That\'s a voice message.\n\n'
            for i in msg_type['voicemsg']:
                msg += str(f'{i} = {voicemsg.__dict__[i]},\n\n')
        elif update.message.reply_to_message.text:
            voicemsg = update.message.reply_to_message.voice
            msg = 'That\'s a text message.\n\n'
    else:
        msg = 'Helloooooo?! This command gives you the info for the MESSAAGE YOU REPLIED TO! You didn\'t even reply to anything!'

    update.message.reply_text(msg)

def add_getmsgtypehandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('getmsgtype', getmsgtype))

def get_command():
    return [BotCommand('getmsgtype','Parker Yeet')]                                                                                                                                                                   