import time
from time import strftime
import tweepy
from twilio.rest import Client
from config import keys

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

keywords = ['parking structure 1', 'parking structure 2', 'm lot',
            'j lot', 'f-5', 'f-10', 'b-lot', 'f-3', 'f-9', 'f-10']


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            print(status.text)
            if any(substring in status.text.lower() for substring in keywords):
                client.messages.create(from_=TWILIO_PHONE_NUMBER,
                                       to=CELL_PHONE_NUMBER,
                                       body=strftime("%a %H:%M") + ' : ' + status.text)
            return True
        except BaseException as e:
            print("Failed on_data :", str(e))
            time.sleep(5)

    def on_error(self, status_code):
        print(status_code)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(async=True, follow=[USER_ID])
