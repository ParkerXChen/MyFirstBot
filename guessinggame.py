from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
from datetime import datetime,timedelta

timein5sec = 0

smallButton = InlineKeyboardButton('Small',callback_data='small')
bigButton = InlineKeyboardButton('Big',callback_data='big')
sumButton = InlineKeyboardButton('Reveal',callback_data='reveal')
joinButton = InlineKeyboardButton('Join',callback_data='join')
startButton = InlineKeyboardButton('Start',callback_data='start')

gamekb = InlineKeyboardMarkup([[bigButton,smallButton,sumButton]])

startkb = InlineKeyboardMarkup([[joinButton,startButton]])


secondspassed = 0 
games = {}

def getNumber():
    endNumber = 0
    msg = ""
    for _i in range(3):
        rnumber = random.randint(1,6)
        endNumber += rnumber
        msg += "%s "%rnumber
    msg += "=%s" % endNumber
    # [11,"1 9 1 = 11"]
    return [endNumber,msg]

def sumGame():
    number,msg = getNumber()
    game = 's'
    if number >= 11:
        game = 'b'
    for u in games.keys():
        if games[u] == '':
            games[u] = 'You did not answer...'
        elif games[u] == game:
            games[u] = 'Won!'
        else:
            games[u] = 'Lost!'
        # print (games[u])
    msg += "\n%s"%getUsers()
    return msg 

def getUsers():
    msg = ""
    for u in games.keys():
        msg += "%s:%s\n"%(u,games[u])
    return msg

def guess(update, context):
    global timein5sec
    timein5sec = datetime.now()+timedelta(seconds=5)
    update.message.reply_text(
    '''
        Press Join. Then press start. Then press Big or Small. Then press reveal.
    .''',reply_markup=startkb)

def buttonCallback(update, context):
    global games,timein5sec
    query = update.callback_query 
    if query.data == 'join':
        query.answer("You have joined the game.")
        games[update.effective_user.first_name] = ""
        query.edit_message_text(getUsers(),reply_markup=startkb)
        return
    elif query.data == 'start':
        timenow=datetime.now()        
        print(f"start now:{timenow} {timein5sec}")
        if datetime.now() >= timein5sec:
            timein5sec = timenow + timedelta(seconds=5)
            query.answer("Round started!")
            query.edit_message_text(getUsers(),reply_markup=gamekb)
        else: 
            query.answer("You cannot start yet! It has been less than 5 seconds since you joined!",show_alert=True)
    elif query.data == 'big':
        if games == {}:
            return
        query.answer("You chose big!")
        games[update.effective_user.first_name] = "b"
        query.edit_message_text(getUsers(),reply_markup=gamekb)
    elif query.data == 'small':
        if games == {}:
            return
        query.answer("You chose small!")
        games[update.effective_user.first_name] = "s"
        query.edit_message_text(getUsers(),reply_markup=gamekb)
    elif query.data == 'reveal':
        timenow = datetime.now()
        print(f"reveal now:{timenow} {timein5sec}")
        if timenow >= timein5sec:
            if games == {}:
                return
            query.answer("Reveal has begun!")
            query.edit_message_text(sumGame())
        else:
            query.answer("You cannot reveal yet! It has been less than 5 seconds since the game started!",show_alert=True)
        

def add_playgamehandler(dp:Dispatcher):
    guess_handler = CommandHandler('playgame', guess)
    dp.add_handler(guess_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback))