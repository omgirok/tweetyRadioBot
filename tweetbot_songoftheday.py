from credentials import *
import tweepy
import random
import datetime
import mysql.connector


# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

x = api.mentions_timeline()
print x

cnx = mysql.connector.connect(user='root', password=pw, database='Music')
cursor = cnx.cursor()
query = "SELECT Songs.Title, Artist.twitter_name FROM Music.Songs, Music.Artist WHERE Songs.Artist = Artist.artist_name AND Artist.twitter_name IS NOT null;"

cursor.execute(query)
songs = cursor.fetchall()
sotd_idx = random.randint(0, len(songs) - 1)

(song, artist) = songs[sotd_idx]

today = datetime.date.today()
try:
	print song, artist
	api.update_status(status="Today's song of the day is " + song + " by " + artist + "! Hope you enjoy :)")

except tweepy.TweepError as e:
	print(e.reason)
	sleep(5)


# for track in trackDict:
# 	try:
# 		if track[4].text != 'Artist':
# 			pass
# 		else:
# 			trackArtist = track[5].text
# 			trackName = track[3].text
# 			print "Song of the day " + datetime.date.strftime(today, '%A, %B %d %Y') 
# 			print trackName + " by " + trackArtist
# 			api.update_status(status="Today's song of the day is " + trackName + " by " + trackArtist + "! Hope you enjoy :)") 
# 			sleep(60*60*24)
# 	except tweepy.TweepError as e:
# 		print(e.reason)
#     sleep(5)