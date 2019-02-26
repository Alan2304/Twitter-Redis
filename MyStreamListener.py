import tweepy
from TtConfig import *
from RedisConfig import *

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, identifier):
        prefix_key = 'i4:'
        composed_key = prefix_key + identifier
        tweepy.StreamListener.__init__(self)
        self.composed_key = composed_key

    def on_status(self, status):
        redis, isConnected = connect()
        if isConnected:
            redis.rpush(self.composed_key, status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print('Disconected ', self.composed_key, '----------------------------------')
            return True #Intenta volver a conectar