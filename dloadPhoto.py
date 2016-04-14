#--------------------------------------------------------------------
# Author: Suryakant Sawant
# Date: 14 April 2016 >>
# Objective: Download image from telegram bot
#
#--------------------------------------------------------------------
import telegram
bot = telegram.Bot(token='my_bot_token') # my token 
bot.getMe() # details about bot

updates = bot.getUpdates()
# to know how many photos are there

# function to return the id's of photos in all updates
def getPhotoId(updates):
	aa = []
	i=0
	for u in updates:
		if u.message.photo:
			aa.append(i)
		i=i+1
	return(aa)
# another quick way to know the id's of photos in all updates
a = [u.message.photo for u in updates]
print(a)

# enter the photo place holder in updates 
jj = updates[19]

jj.to_dict()
"""
# Note that photos are available in three different sizes
# 1. small, 2. medium, 3. original
{'message': 
	{'from': 
		{'username': u'Suryakant54321', 'first_name': u'Suryakant', 'last_name': u'Sawant', 'id': xxxxxxx}, 
			'photo': 
				[{'width': 90, 'height': 36, 'file_id': 'xxxxxxx', 'file_size': 902},
				{width': 320, 'height': 128, 'file_id': 'xxxxxxx', 'file_size': 11151}, 
				{'width': 652, 'height': 260, 'file_id': 'xxxxxxx', 'file_size': 29875}],
			'chat': {'username': u'Suryakant54321', 'first_name': u'Suryakant', 'last_name': u'Sawant', 'type': u'private', 'id': xxxxxxx},
			'date':1460567841, 
			'message_id': xx},

'update_id': xxxxxxx}
"""
f_id = jj.to_dict()['message']['photo'][0]['file_id']#put photo identifier 0=small, 1=medium, 2=original
newFile = bot.getFile(f_id)
newFile.download('File_path\\file4.jpg')

