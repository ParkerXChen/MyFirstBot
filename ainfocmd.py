from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
from json import dumps

def ainfo(update,context):
    msg =  f'File ID: {update.message.reply_to_message.document.file_id},\nFile Unique ID: {update.message.reply_to_message.document.file_unique_id},\nFile Type: {update.message.reply_to_message.document.mime_type},\nFile Size: {update.message.reply_to_message.document.file_size} '
    
    update.message.reply_text(msg)

def add_ainfohandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('ainfo', ainfo))

def get_command():
    return [BotCommand('ainfo','看看你的金币有没有丢失')]