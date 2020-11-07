from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import rewards
import guesscmd

def start(update, context):
    print(update)
    msg = "%s你好，你在%s说话"%(
        update.message.from_user.first_name,
        update.message.chat.type
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

rewards.add_handler(dispatcher)
guesscmd.add_handler(dispatcher)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()