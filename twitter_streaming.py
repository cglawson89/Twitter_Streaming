#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "47869870-ir9IZ5bAfvHobc2FPbzZ6HW6uMlKGaFKuwz72mSpt"
access_token_secret = "JvPzTgAIIPSCcg75Wn5h5Iv4eZ0sf0lyxlB6QsG64cagg"
consumer_key = "0bNiyAkPfAIpnBT78AGW5GsU6"
consumer_secret = "GXk9U1Z8ijHIwe5mBWcztsnNK0od8ZbmbTnn0UKh8XpN4SQ3Nu"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
