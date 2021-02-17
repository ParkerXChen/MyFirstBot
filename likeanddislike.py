from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, MessageHandler, CallbackQueryHandler, CommandHandler, filters

uservote = {}

def reaction(update,context):
    message = update.channel_post
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("Like 👍(0)",callback_data="channelvote:👍:0"),
        InlineKeyboardButton("Dislike 👎(0)",callback_data="channelvote:👎:0"),
        ]])
    message.edit_reply_markup(reply_markup = kb)

def add_user_vote(msgid,uid,vote):
    if not msgid in uservote :
        uservote[msgid] = {}
    if not uid in uservote[msgid] :
        uservote[msgid][uid] = vote
        return True 
    return False

def add_vote(button,i):
    cmd = button.callback_data.split(":")
    count = int(cmd[2]) + i
    if cmd[1] == "👍":
        return InlineKeyboardButton(f"Like 👍({count})",callback_data=f"channelvote:👍:{count}")
    else:
        return InlineKeyboardButton(f"Dislike 👎({count})",callback_data=f"channelvote:👎:{count}")


def react_callback(update,context):
    query = update.callback_query
    cmd = query.data.split(":")
    buttons = query.message.reply_markup.inline_keyboard
    msgid = query.message.message_id
    uid = update.effective_user.id
    vote = cmd[1]

    if add_user_vote(msgid,uid,vote) :
        count = int(cmd[2]) + 1
        
        if cmd[1] == '👍':
            query.answer("Liked!")
            buttons[0][0] = InlineKeyboardButton(f"Like 👍({count})",callback_data=f"channelvote:👍:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        elif cmd[1] == "👎":
            query.answer("Disliked!")
            buttons[0][1] = InlineKeyboardButton(f"Dislike 👎({count})",callback_data=f"channelvote:👎:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        if vote == uservote[msgid][uid]:
            count = int(cmd[2]) - 1
            if cmd[1] == '👍':
                query.answer("Unliked!")
                buttons[0][0] = InlineKeyboardButton(f"Like 👍({count})",callback_data=f"channelvote:👍:{count}")
                del uservote[msgid][uid]
            elif cmd[1] == "👎":
                query.answer("Undisliked!")
                buttons[0][1] = InlineKeyboardButton(f"Dislike 👎({count})",callback_data=f"channelvote:👎:{count}")
                del uservote[msgid][uid]
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        else:
            if cmd[1] == "👍":
                buttons[0][0] = add_vote(buttons[0][0],1)
                buttons[0][1] = add_vote(buttons[0][1],-1)
            else:
                buttons[0][1] = add_vote(buttons[0][1],1)
                buttons[0][0] = add_vote(buttons[0][0],-1)
            uservote[msgid][uid] = vote
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))

def add_handler(dp:Dispatcher):
     dp.add_handler(MessageHandler(filters = filters.Filters.all, callback=reaction))
     dp.add_handler(CallbackQueryHandler(react_callback,pattern="^channelvote:[A-Za-z0-9_:]*"))