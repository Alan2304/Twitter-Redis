import tweepy

#Llaves de autentificación
consumer_key = 'Your Consumer key'
consumer_secret = 'Your consumer secret'

access_token = 'Your Access token'
access_token_secret = 'Your Secret Token'

def conectTt():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

