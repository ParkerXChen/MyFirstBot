from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
from json import dumps

def ainfo(update,context):
    print (update)
    msg =  f'File Size : {update.message.reply_to_message.animation.file_size},\nFile Name: {update.message.reply_to_message.animation.file_name},\nDuration: {update.message.reply_to_message.animation.duration},\nWidth: {update.message.reply_to_message.animation.width},\nHeight: {update.message.reply_to_message.animation.height}'
    
    update.message.reply_text(msg)

def add_ainfohandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('ainfo', ainfo))

def get_command():
    return [BotCommand('ainfo','看看你的金币有没有丢失')] 