from datetime import datetime,timedelta

timenow = datetime.now()
timein5sec = datetime.now() + timedelta(seconds=5)

print(f"{timenow} + 5 seconds = {timein5sec}")

timenow2 = datetime.now()

print(f"{timenow2} : {timenow2 > timenow} : {timenow2 > timein5sec}")



"""
/guess command run

    time5sec


click start button

    datetime.now()>= time5sec

query.answer("等等",show_alert=Ture






/playgame command  time5sec

    join
    join
    join

click start_button  now > time5sec  &&  reset time5sec

clieck reveal_button now > time5sec

"""