from credentials import *
import tweepy

# Save keys/secrets to variables
# consumer_key = 'your_key_here'
# consumer_secret = 'your_key_secret'
# access_token = 'your_token_here'
# access_token_secret = 'your_secret_here'


# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = 'Hello, world!'
# api.update_status(status=tweet)

print api.me()