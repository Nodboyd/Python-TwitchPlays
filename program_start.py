#Run This File to Start After Everything is Setup!
#Make Sure You add Your Info Into userinfo.py!
#Make Sure You Add Sockets Library 
import timer
import TwitchController


# This starts the 5 second countdown, if you want an instant start just remove this line!
# You can make the countdown longer in timer.py
timer.stopwatch()


# This launches the twitch controller
# If you want to make this easier on your self
# I reccomend changing the name of TwitchController.py to something else like MinecraftController.py
# and putting all your minecraft commands in there.
# Then you can create a GameBoyControoler.py file
# and put all your gameboy commands in there.
# This way you don't need to keep remaking the file over and over again.

# You will only need to update the import line on line 5 to be the name of your new file
# ex) import MinecraftController

# Then update the command below this to be the name of your new file
# ex) MinecraftController.program()
TwitchController.program()

