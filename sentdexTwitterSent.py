from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="xNjTg6GU87D2zmPlVV8h4EccP"
csecret="lPPLUtHOs7MdWuZm2HG4aE7STZid4QZVdgYl3RiNBdUbRBFCwh"
atoken="18593973-SPfJ0L4PDYP5UebUX4YSpVwSal1NUGLWB9FSZ8EYJ"
asecret="6y106J4ftAI42QFk6awgGKqJNemiqL9dOr9hTRCXrZanZ"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet,sentiment_value,confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])