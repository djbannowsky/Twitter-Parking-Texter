import tweepy
from twilio.rest import Client
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
USER_ID = keys['user_id']
ACCOUNT_SID = keys['account_sid']
AUTH_TOKEN = keys['auth_token']

TWILIO_PHONE_NUMBER = keys['twilio_phone_number']
CELL_PHONE_NUMBER = keys['cell_phone_number']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

client = Client(ACCOUNT_SID, AUTH_TOKEN)
