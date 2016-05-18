"""
#-----------------------------------------------------------------------
# Author: Suryakant Sawant
# Date: 18 May 2016
# Objective: 1. added GetCapability parser
# Testing on: 
# 1. National Data Buoy Center (http://sdf.ndbc.noaa.gov/sos/server.php)
# 2. ISTSOS Demo database (http://istsos.org/istsos/demo)
#-----------------------------------------------------------------------
"""
import re, os, fnmatch
from colorama import Fore, Back, Style
import xmltodict
import requests
#-----------------------------------------------------------------------
def parseSOScap(url):
	"""
	url [str] URL / service GetCapabilities request
	output dict of service details
	To Do: Catch response, Parse Response, Form Dict
	"""
	detailsDict ={} # e.g. detailsDict['water']=100
	# import request class
	import requests as requests
	# Check and verify Get Capabilities request
	verify = verifyGCReq(url)
	if verify == 'VALID':
		# Send request
		res = requests.get(url)
		#print(res, res.text)
		# Catch response
		# Parse Response
		# Form Dict
		try:
			jj = xmltodict.parse(res.text)
			soWasted = jj['Capabilities']['Contents']['ObservationOfferingList']['ObservationOffering']
			# list all sensors
			for i in range(len(soWasted)):
				print (soWasted[i]['@gml:id'])
		except:
			pass
		try:
			jj = xmltodict.parse(res.text)
			soWasted = jj['sos:Capabilities']['sos:Contents']['sos:ObservationOfferingList']['sos:ObservationOffering']
			for i in range(len(soWasted)):
				print (soWasted[i]['@gml:id'])
		except:
			pass
	#print(Fore.RED+"Some Error in Get Capabilities parsing"+Fore.RESET)
	elif verify == 'INVALID':
		print(Fore.RED+"URL is Invalid check URL content for 'http:','request','getcapabilities', 'SOS' and 'service'"+Fore.RESET)	
	else:
		print(Fore.RED+"There is unknown problem with URL"+Fore.RESET)
	return detailsDict
#-----------------------------------------------------------------------
def verifyGCReq(url):
	"""
	Check and verify Get Capabilities request

	url [str] URL / service GetCapabilities request
	
	output VALID/ INVALID / ERROR
	"""
	verify = "ERROR"
	splitURL = re.split("/|=|&|\\?|\\.", url)
	for i in range(len(splitURL)): splitURL[i] = splitURL[i].lower()
	print(splitURL)
	findThis = ['http:','request','getcapabilities', 'sos', 'service']
	foundThis = []
	for i in range(len(findThis)):
		me = fnmatch.filter(splitURL, '*'+findThis[i]+'*')
		if me != []:
			foundThis.append(me[0])
	if len(findThis) == len(foundThis):
		verify = "VALID"
	else:
		verify = "INVALID"
	#print (findThis)
	#print (foundThis)
	return verify
#-----------------------------------------------------------------------
# implementation

# To do
# 1. Push data through Telegram Bot
# 2. Check feasibility for localhost

#Approach 3
# List of things I need from Get Observation Request
# 1. Name of offering
# 2. coordinates
# 3. TimePeriod (beginPosition, endPosition)
# 4. observedProperty (1, ... n)
# 5. featureOfInterest 
 
url = 'http://istsos.org/istsos/demo?request=getCapabilities&section=contents&service=SOS'
url2 = 'http://sdf.ndbc.noaa.gov/sos/server.php?request=GetCapabilities&service=SOS' 

parseSOScap(url2)

