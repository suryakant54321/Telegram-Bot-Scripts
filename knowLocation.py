#--------------------------------------------------------------------
# Author: Suryakant Sawant
# Date: 14 April 2016 >>
# Objective: Read location messages from telegram bot
#
#--------------------------------------------------------------------
import telegram
bot = telegram.Bot(token='TOKEN') # my token 
bot.getMe() # details about bot

updates = bot.getUpdates()
# function to return the id's of locations in all updates
def getLocationId(updates):
	aa = []
	i=0
	for u in updates:
		if u.message.location:
			aa.append(i)
		i=i+1
	return(aa)
# usage
aa = getLocationId(updates)

# another quick way to know the location id's
a = [u.message.location for u in updates]
print(a)

# enter the photo place holder in updates 
kk = updates[aa[0]]
kk.to_dict()
"""
{'message': 
	{'from': 
		{'username': u'Suryakant54321', 'first_name': u'Suryakant', 'last_name': u'Sawant', 'id': xxxxxxx}, 
	'location': 
		{'latitude': 19.132253, 'longitude': 72.917923}, 
	'chat': 
	{'username': u'Suryakant54321', 'first_name': u'Suryakant','last_name': u'Sawant', 'type': u'private', 'id': xxxxxxx}, 
	'date': 1460532910, 
	'message_id': xx}, 
'update_id': xxxxxxx}
"""
aa = getLocationId(updates)
# iterate through all locations
for i in range(0,len(aa)):
	kk = updates[aa[i]]
	print(kk['message']['location'])
#


