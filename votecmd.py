from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton
import random

# messageid: [uid,uid,uid...]
# messageid: {uid:'like'/'dislike',uid:'like'/'dislike'...}
uservote = {}

def vote(update,context):
    gifs = [
        ['https://thumbs.gfycat.com/OrganicCelebratedFlatcoatretriever-max-1mb.gif', 'He just got hungry...'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-bike-ramp.gif', 'Do NOT try this at home'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-soccer-reporter-hit-in-head.gif', 'He gets a yellow for that, right?'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-gymnastics.gif', 'Maybe we should ground that...'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-hockey-glass.gif', 'What was that made of?! Glass?!'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-punching-yourself.gif', 'Stop punching yourself... Stop punching yourself...'],
        ['https://media1.giphy.com/media/lXiRlunRf4T1bDkaI/source.gif', 'Hey, How was I suposed to know it was frozen?!'],
        ['https://wanna-joke.com/wp-content/uploads/2013/03/fail-gif1.gif', 'I thought it was just a puddle...'],
        ['https://68.media.tumblr.com/fb84a01c8a4acf349cf9a0a5ee608ea9/tumblr_o1mtlzwQ1v1tdsuf5o1_500.gif', 'Headshot Bonus!'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/10/water-balloon-fail.gif', 'That is NOT a water balloon.'],
        ['https://i.chzbgr.com/full/5560084736/hEF066B39/double-skate-fail', 'Maybe I should start with the curb...'],
        ['https://i.chzbgr.com/full/4102161664/hBC1CB70A/soccer-fail', 'Post!'],
        ['https://media1.giphy.com/media/rW6CpFhDj9lkc/200.gif', 'Hey, you crossed the foul line!'],
        ['https://gifscenter.com/wp-content/uploads/2017/05/funny%20kid%%20fail%%20gif.gif', 'a'],
        ['https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-basketball-trick.gif', 'a'],
        ['https://media4.giphy.com/media/WbhKnXKLZAkVi/source.gif', 'a'],
        ['https://i.pinimg.com/originals/2f/be/a3/2fbea3d75a9a437e6541beb32d34684c.gif', 'a'],
        ['https://media2.giphy.com/media/l41lFYeLmNE4DZP6U/source.gif', 'a'],
        ['https://i.pinimg.com/originals/ef/c6/0b/efc60b0c103c21f746fd0f105ec68dad.gif', 'a'],
        ['https://www.humoar.com/wp-content/uploads/gallery/gymfails/01.gif', 'a']
    ]
    #  [[👍,👎]]
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("Like 👍(0)",callback_data="vote:👍:0"),
        InlineKeyboardButton("Dislike 👎(0)",callback_data="vote:👎:0"),
        ]])
    gif = random.choice(gifs)
    update.message.reply_animation(gif[0],caption=gif[1],reply_markup=kb)

def add_user_vote(msgid,uid,vote):
    # parker not vote
    # like or dislike +1

    # parker vote like
    # if vote like then like -1 
    # if vote dislike then  like -1  dislike +1

    if not msgid in uservote :
        uservote[msgid] = {}
    if not uid in uservote[msgid] :
        uservote[msgid][uid] = vote
        return True # 之没投过
    return False # 之前投过票

def add_vote(button,i):
    cmd = button.callback_data.split(":")
    count = int(cmd[2]) + i
    if cmd[1] == "👍":
        return InlineKeyboardButton(f"Like 👍({count})",callback_data=f"vote:👍:{count}")
    else:
        return InlineKeyboardButton(f"Dislike 👎({count})",callback_data=f"vote:👎:{count}")


def vote_callback(update,context):
    query = update.callback_query
    cmd = query.data.split(":") # ['vote','👍',0]
    buttons = query.message.reply_markup.inline_keyboard
    msgid = query.message.message_id
    uid = update.effective_user.id
    vote = cmd[1]

    if add_user_vote(msgid,uid,vote) :
        print (uservote)
        count = int(cmd[2]) + 1
        
        if cmd[1] == '👍':
            query.answer("Liked!")
            buttons[0][0] = InlineKeyboardButton(f"Like 👍({count})",callback_data=f"vote:👍:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        elif cmd[1] == "👎":
            query.answer("Disliked!")
            buttons[0][1] = InlineKeyboardButton(f"Dislike 👎({count})",callback_data=f"vote:👎:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        if vote == uservote[msgid][uid]:
            print (uservote)
            count = int(cmd[2]) - 1
            if cmd[1] == '👍':
                query.answer("Unliked!")
                buttons[0][0] = InlineKeyboardButton(f"Like 👍({count})",callback_data=f"vote:👍:{count}")
                del uservote[msgid][uid]
            elif cmd[1] == "👎":
                query.answer("Undisliked!")
                buttons[0][1] = InlineKeyboardButton(f"Dislike 👎({count})",callback_data=f"vote:👎:{count}")
                del uservote[msgid][uid]
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        else:
            print (uservote)
            if cmd[1] == "👍":
                buttons[0][0] = add_vote(buttons[0][0],1)
                buttons[0][1] = add_vote(buttons[0][1],-1)
            else:
                buttons[0][1] = add_vote(buttons[0][1],1)
                buttons[0][0] = add_vote(buttons[0][0],-1)
            uservote[msgid][uid] = vote
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('vote', vote))
    dp.add_handler(CallbackQueryHandler(vote_callback,pattern="^vote:[A-Za-z0-9_:]*"))

def get_command():
    return [BotCommand('vote','Like or Dislike a GIF!')]