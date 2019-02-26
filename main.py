import redis
from MyStreamListener import *
from RedisConfig import *
from TtConfig import *
import time
import sys

def obtainKeys(keys):
    redis, isConnected = connect()
    if isConnected:
        return redis.keys(pattern=keys)

def countValues(key):
    redis, isConnected = connect()
    if isConnected:
        return redis.llen(key)

def trendings():
    topics = []
    keysArray = obtainKeys('i4:*')
    for key in keysArray:
        nTweets = int(countValues(key))
        topics.append((key, nTweets))
    
    sortedTrendings = sorted(topics, key=lambda number: number[1], reverse=True)
    return sortedTrendings

def main(): 
    apiTt = conectTt()
    streamListenerIot = MyStreamListener('iot')
    myStreamIot = tweepy.Stream(auth = apiTt.auth, listener=streamListenerIot)
    myStreamIot.filter(track=['internet of things', 'iot'], is_async=True)
    
    streamListenerSec = MyStreamListener('cybersecurity')
    myStreamSec = tweepy.Stream(auth = apiTt.auth, listener=streamListenerSec)
    myStreamSec.filter(track=['cybersecurity', 'cyber security'], is_async=True)

    streamListenerCloud = MyStreamListener('cloud_computing')
    myStreamCloud = tweepy.Stream(auth = apiTt.auth, listener=streamListenerCloud)
    myStreamCloud.filter(track=['cloud computing', 'cloudcomputing'], is_async=True)

    while 1:
        try:
            trending = trendings()
            print(time.ctime()) #Imprime la fecha y hora del sistema
            i = 1
            for theme in trending:
                print(i, '- ', theme)
                i += 1

            print('-----------------------------')
            time.sleep(3) #Espera 3 segundos para no saturar la linea de comandos
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

main()