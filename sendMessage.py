#--------------------------------------------------------------------
# Author: Suryakant Sawant
# Date: 14 April 2016 >>
# Objective: Send message (text, image and location) to telegram bot
#
#--------------------------------------------------------------------
import telegram, datetime, time
bot = telegram.Bot(token='my_bot_token') # my token 
bot.getMe() # details about bot

# Get chat id is must
chat_id = bot.getUpdates()[-1].message.chat_id

# 1. Send text message
msgContent = ("this is message sent on '%s' ")%(time.ctime())
bot.sendMessage(chat_id=chat_id, text=msgContent)

# 2. send image message
# from URL
bot.sendPhoto(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')

# Locate file from Disk
f = open('file_path\\I_Am_Free.jpg', 'rb')
# Send
bot.sendPhoto(chat_id=chat_id, photo=f)

# 3. Send location message
bot.sendLocation(chat_id=chat_id, latitude='19.132253', longitude='72.917923')

# To Do:
# Find IP of GSM network
# Find approx. lat lon for given IP 
# Send location to telegram bot

