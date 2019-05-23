from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import sentiment_mod as s 
import json

#consumer key, consumer secret, access token, access secret.
ckey="AU71zSX6iMo0vXUaRwrob767j"
csecret="QAMPh1z2ag90Be6QstZEGBwwvyphUYvyQesdCrlApJAvFN2sJh"
atoken="1131602676616224768-5xrABa8WI8qfQfr6BmmfJ2TCtQdkWE"
asecret="ouuwO1KqaXDTWCC2KxKoE5lrkuZjlUPRcMhKQUFz3KTiq"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
           output = open("twitter-out.txt","a")
           output.write(sentiment_value)
           output.write('\n')
           output.close()  

        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])

