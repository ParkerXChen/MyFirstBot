from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
from json import dumps

def pinfo(update,context):
    msg =  f'File ID: {update.message.reply_to_message.photo.file_id},\nFile Unique ID: {update.message.reply_to_message.photo.file_unique_id},\nFile Width: {update.message.reply_to_message.photo.width},\nFile Height: {update.message.reply_to_message.photo.height},\nFile Size: {update.message.reply_to_message.photo.file_size}'
    
    update.message.reply_text(msg)

def add_pinfohandler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pinfo', pinfo))

def get_command():
    return [BotCommand('pinfo','看看你的金币有没有丢失')]