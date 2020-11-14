from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import random
from datetime import datetime,timedelta
import coins

smallButton = InlineKeyboardButton('Small',callback_data='small')
bigButton = InlineKeyboardButton('Big',callback_data='big')
sumButton = InlineKeyboardButton('Reveal',callback_data='sum')
GetCoinsButton = InlineKeyboardButton('Get Coins',callback_data='GetCoins')

gamekb = InlineKeyboardMarkup([[bigButton,smallButton,sumButton]])

joinButton = InlineKeyboardButton('Join',callback_data='join')
startButton = InlineKeyboardButton('Start',callback_data='start')

startkb = InlineKeyboardMarkup([[joinButton,startButton,GetCoinsButton]])

timer = 0

games = {}

def check_chatid(chatid):
    if not chatid in games.keys():
        games[chatid]={
            "h":"",
            "p":{}
            }

def getHist(chatid):
    return games[chatid]['h']

def setHist(chatid,res):
    h = games[chatid]['h']
    if len(h) > 10:
        h = h[:9] + res
    else:
        h += res
    games[chatid]['h'] = h

def getNumber():
    endNumber = 0
    msg = ""
    for _i in range(3):
        rnumber = random.randint(1,6)
        endNumber += rnumber
        msg += "%s "%rnumber
    msg += "=%s" % endNumber
    return [endNumber,msg]

def sumGame(chatid):
    number,msg = getNumber()
    users = games[chatid]["p"]
    game = 's'
    if number >= 11:
        game = 'b'
    setHist(chatid,game)
    for u in users.keys():
        if users[u] == '':
            users[u] = 'Did not answer...'
        elif users[u] == game:
            users[u] = 'Win!'
        else:
            users[u] = 'Lose!'
    msg += "\n%s"%getUsers(users)
    return msg 

def getUsers(users):
    msg = ""
    for u in users.keys():
        print(u)
        msg += "%s:%s\n"%(u.first_name,users[u])
    return msg

def guess(update, context):
    global timer
    chatid = update.effective_chat.id
    check_chatid(chatid)
    timer = datetime.now() + timedelta(seconds=5)
    update.message.reply_text("Please select large or small",reply_markup=startkb)

def buttonCallback(update, context):
    global games,timer
    query = update.callback_query 
    chatid = update.effective_chat.id
    user = update.effective_user
    check_chatid(chatid)
    users = games[chatid]["p"]
    msg = getUsers(users) + "\n\n" + getHist(chatid)
    if query.data == 'join':
        query.answer("Join the game")
        users[update.effective_user] = ""
        query.edit_message_text(msg,reply_markup=startkb)
        return
    elif query.data == "daily":
        c = coins.daily(chatid,user)
        if c == 0:
            query.answer("Oops, You have to wait a little bit!",show_alert=True)
        else:
            query.answer(f"You won {c} Coins!",show_alert=True)
    elif query.data == 'start':
        timenow = datetime.now()
        if timenow > timer:
            query.answer("Begin")
            query.edit_message_text(msg,reply_markup=gamekb)
            timer = datetime.now()+timedelta(seconds=5)
        else:
            query.answer("Woah, Woah! Wait for like, 5 seconds!",show_alert=True)
    elif query.data == 'big':
        if users == {}:
            return
        query.answer("You Chose big")
        users[update.effective_user] = "b"
        query.edit_message_text(msg,reply_markup=gamekb)
    elif query.data == 'small':
        if users == {}:
            return
        query.answer("You chose small")
        users[update.effective_user] = "s"
        query.edit_message_text(msg,reply_markup=gamekb)
    elif query.data == 'sum':
        timenow = datetime.now()
        if timenow > timer:
            query.answer("Reveal has begun!")
            msg = sumGame(chatid)+ "\n\n" +getHist(chatid)
            query.edit_message_text(msg)
            users = {}
        else:
            query.answer("Woah, Woah! Wait for like, 5 seconds!",show_alert=True)
    games[chatid]["p"] = users

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('guess', guess))
    dp.add_handler(CallbackQueryHandler(buttonCallback))