from credentials import *
import tweepy
from time import sleep
import xml.etree.ElementTree as ET
import random

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tree = ET.parse('Library.xml')
root = tree.getroot()

nav = root.find('dict')
nav = nav.find('dict')

trackDict = nav.findall('dict')
random.shuffle(trackDict)
for track in trackDict:
	try:
		if track[4].text != 'Artist':
			pass
		else:
			trackArtist = track[5].text
			trackName = track[3].text
			print trackName + " by " + trackArtist
			api.update_status(status="Today's song of the day is " + trackName + " by " + trackArtist + "! Hope you enjoy :)") 
			sleep(60*60*24)
	except tweepy.TweepError as e:
		print(e.reason)
        sleep(5)