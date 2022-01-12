#Required Libraries
import socket
import threading
import userinfo
import time
import twitchlogo
#Recogmended Libraries
import random
import pyautogui
import keyboard
import mouse


global special_char
global capital_char
global command_cooldown
command_cooldown = []
special_char = ['!','@',"#","$","%","^","&","*","(",")","?",]
capital_char = ['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

message = ' '
user = ' '


# This is to connect to the IRC Client You don't need to change this!
# Changing any of this will break the program!
# You're better off just ignoring this part of the code!
# Skip to line 44 to see what you can to change!
def program():
    twitchlogo.print_twitch_logo()
    SERVER = "irc.twitch.tv"
    PORT = 6667
    PASS = userinfo.PASS
    BOT = userinfo.BOT
    CHANNEL = userinfo.CHANNEL
    OWNER = userinfo.OWNER
    irc = socket.socket()
    irc.connect((SERVER, PORT))
    irc.send((	"PASS " + PASS + "\n" +
                "NICK " + BOT + "\n" +
                "JOIN #" + CHANNEL + "\n").encode())

# ----------------------------------------------------------------------------------------------------------------------
# These are preset commands to make life easier!


    #Example of Twitch Bot Commands Setup
    # This is the section you can edit to add more commands to your bot
    # You can add as many commands as you want, but make sure you add the command in the format of:
    # If message.lower() == "command":

    #Example if you want a command that would make you move forward for 5 seconds
    # You would add this command to the program:
    # if message.lower() == "moveforward":
    #     PressAndHoldKey("w", 5)
    #     return ""



    def gamecontrol():
        global message
        global user
        

        # This command presses the given button for the given amount of time
        # ex) PressAndHoldKey("w", 5)
        # This would press the w key for 5 seconds
        
        # The keys should be given in lowercase and if you are unsure of a key
        # name you can find them through the documenation of keyboard > https://github.com/boppreh/keyboard#api
        # There is currently no way to distinguish between different keys with the same name such as numpad and number keys
        # There is no current attempt to make this work with multiple keys with this library
        def PressAndHoldKey(key, seconds):
            keyboard.press(key)
            time.sleep(seconds)
            keyboard.release(key)


        # This command works the samem as PressAndHoldKey but instead it presses 2 keys at the same time
        # ex) PressAndHoldKeys("w", "a", 5)
        # This would press the w and a key for 5 seconds

        # The keys should be given in lowercase and if you are unsure of a key
        # name you can find them through the documenation of keyboard > https://github.com/boppreh/keyboard#api
        def PressAndHold2Key(key1,key2,seconds): 
            keyboard.press(key1)
            keyboard.press(key2)
            time.sleep(seconds)
            keyboard.release(key1)
            keyboard.release(key2)


        # This command simply holds down a key indefinetly
        # It is useful for when you want to hold down a key for an undetermined amount of time
        # ex) HoldKey("w")
        # This would hold the w key down indefinetly
        def HoldKey(key):
            keyboard.press(key)

        # This command releases a key that is currently held down
        # ex) ReleaseKey("w")
        # This would release the w key
        # This command is most useful when a key has gone through the HoldKey function
        # and you want to release it
        def ReleaseKey(key):
            keyboard.release(key)


        # This command uses the mouse libary to click the mouse at the current mouse position 
        # For a given amount of time, with either the left or right mouse button
        # ex) MouseClick("left", 5)
        # This would hold the left mouse button for 5 seconds
        def MouseClick(key,seconds):#key means left or right for this one
            mouse.press(button = key)
            #Mouse has a timer otherwise left click may not get registered. In some games it can be 0.1 seconds
            time.sleep(seconds)
            mouse.release(button = key)
    

        # This is an example command on how to move the mouse
        # It moves the mouse relative to the current mouse position
        # In the given direction from the x and y coords given
        # It is important to note that the seconds should not be short otherwise the mouse
        # will not be able to move to the new position completely
        # ex) MouseMove(100,100,5) 
        # This would move the mouse relative to the current mouse position by 100 pixels in the x direction and 100 pixels in the y direction
        # So this would move the mouse to the right 100 pixels and down 100 pixels (You will need to find values that work for your game)
        def MouseTurn(x,y,seconds):
            pyautogui.moveRel(x,y,seconds)
            return
            
        
        # If you don't want your command to run every time the command message is recieved
        # you can add action chance before the command to make it more random if the command will run or not
        # You can find an examble in the section below under the forward example! 
        def ActionChance(x,y):
            chance = random.randint(x,y)
            return chance



        while True:

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Keyboard Commands Section            

            # This command is a general purpose forward command
            # It presses the w key for a set amount of time
            # It first goes through the action chance command to make sure the command is not over used by chat
            # It bassicaly gives it a 50/50 chance of running
            # If the action chance works then it will run the command and pressandhold the w key for 5 seconds
            if message.lower() == 'forward' or message.lower() == 'w':
                #50% chance Command will run. Runs on Odd Numbers 
                if ActionChance(1,10) % 2 == 0:
                    break
                PressAndHoldKey('w',5)
                return


            # This command is a general purpose back command
            # It presses the s key for a set amount of time
            # It first goes through the action chance command to make sure the command is not over used by chat
            # This one is harder to get through
            # There is a 1 in 10 chance of running the command
            # You can change the number on the right to change the odds of running the command
            if message.lower() == 'back' or message.lower() == 's':
                #10% Chance command will run
                if ActionChance(1,10) == 1:
                    break
                PressAndHoldKey('s',2)
                return

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# These are more general purpose commands that can be used to make the bot do more than just move forward and back
# There are no action chances these commands will always run reguardless of how often it is said in chat
            if message.lower() == 'left' or message.lower() == 'port' or message.lower() == 'a':
                PressAndHoldKey('a',10)
                return

            if message.lower() == 'right' or message.lower() == 'starboard' or message.lower() == 'd':
                PressAndHoldKey('d',10)
                return

            if message.lower() == 'jump':
                PressAndHoldKey('space',2)
                return

            if message.lower() == 'crouch':
                PressAndHoldKey('shift',2)
                return

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This is a command where hold key is useful
            # This command is meant for minecraft but can be altered easily
            # It goes through an action chance command to make sure the command is not over used by chat ( this can just be removed if you don't want it )
            # It then preses the games run button and holds it down indefinetly
            # Then it presses the direction key for a set amount of time
            # Then releases the run button after the direction key
            if message.lower() == 'run' or message.lower() == 'sprint': 
                if ActionChance(1,2) == 2:
                    break
                HoldKey('control')
                PressAndHoldKey('w',2)
                ReleaseKey('control')

                return
# Mouse Movement Section 
# ----------------------------------------------------------------------------------------------------------------------
            #You may need to experiment with turning angles and time. This turns you about 90° to the right in MC
            if message.lower() == 'turn right':
                MouseTurn(60,0,1)
                return
            
            if message.lower() == 'left click':
                MouseClick('left',2)
                return

            else:
                message == ''
                return
            message=''  
            return
# ----------------------------------------------------------------------------------------------------------------------
    # Connects You to Twitch Servers and starts other groups (i.e Controller and Commands)
    # You Should Not Need to Change Anything in this section
    # For real you probably don't even need to look at this section...
    # Changing stuff here will either do nothing or will break the bot
    # I truly don't even understand whats going on here but I have to put it here so it works
    # There are many better ways to do this but this is what I came up with a few years ago and it works
    # If I ever understand how to use the Twitch PubSub API I will remove this section and replace it with a better way to do this
    # That will make the bot better in general because it would allow sub only commands and other things
    # If you have any idea how to use pubsub in python I would be happy to know
    # My email is henryfundenberger@gmail.com
    #-----------------------------------------------------------------------------------------------------------------------
    def twitch():
        
        global user
        global message

        def joinchat():
            Loading = True
            while Loading:
                readbuffer_join = irc.recv(1024)
                readbuffer_join = readbuffer_join.decode()                
                for line in readbuffer_join.split("\n")[0:-1]:                    
                    Loading = loadingComplete(line)
        def loadingComplete(line):
            if("End of /NAMES list" in line):
                #sendMessage(irc, "Hello World!")
                return False
            else:
                return True
        global sendMessage
        def sendMessage(irc, message):
            messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
            irc.send((messageTemp + "\n").encode())
        def getUser(line):
            global user
            colons = line.count(":")
            colonless = colons-1
            separate = line.split(":", colons)
            user = separate[colonless].split("!", 1)[0]
            return user
        def getMessage(line):
            global message
            try:
                colons = line.count(":")
                message = (line.split(":", colons))[colons]
            except:
                message = ""
            return message
        def console(line):
            if "PRIVMSG" in line:
                return False
            else:
                return True
        while True:
            try:
                readbuffer = irc.recv(1024).decode()
            except:
                readbuffer = ""
            for line in readbuffer.split("\r\n"):
                if line == "":
                    continue
                if "PING :tmi.twitch.tv" in line:
                    msgg = "PONG :tmi.twitch.tv\r\n".encode()
                    irc.send(msgg)
                    continue
                else:
                    global user
                    user = getUser(line)
                    message = getMessage(line)
                    if user == "" or user == " ":
                        continue
                    print(user.title() + " : " + message)
                    t2 = threading.Thread(target = gamecontrol)
                    t2. start()       
        
    t1 = threading.Thread(target = twitch)
    t1.start()
# -----------------------------------------------------------------------------------------------------------------------