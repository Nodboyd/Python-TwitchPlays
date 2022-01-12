# Never Show This Information To Anybody, Your Twitch OAuth Token is Used to Connect to Your Twitch Account!
# Get Your Oauth Token Here -> https://twitchapps.com/tmi/
# Place Oauth Token Here in Entirety, Make sure you're signed in on twitch as your bot then get your oauth token!
# ex) PASS = "oauth:AVeryLongStringofNumbersAndLetters"
# Make sure you are logged into the account on twitch that you want sending messages!
PASS = "oauth:AVeryLongStringofNumbersAndLetters"

# Place the name of the account you want sending messages to here!
# For example I dont want my main account to be the one sending messages 
# So I logged into twitch with my bot account and got my oauth token under my bots account
# Thats the account name I'm putting here!
BOT = "myBotName"
BOT = BOT.lower()

# Your Channel Name
# This is the channel you want to connect to!
CHANNEL = "myChannelName"
channel = CHANNEL.lower()

# Your Bots Name or Your Channel Name 
# This makes the program ignore this user!
# Or leave empty quotes if you dont want to ignore any users!
OWNER = "mychannelname" 
OWNER = OWNER.lower()
