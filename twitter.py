from config import *
import time
from time import strftime

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
