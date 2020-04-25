from stockbot import *
import tweepy
import time
import csv
import random
from os import environ

INTERVAL = 15

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


nasdaqFile = open('EODnasdaq.csv', 'r')
nasdaqReader = csv.reader(nasdaqFile)
nasdaqRows = [r for r in nasdaqReader]
nasdaqLength = len(nasdaqRows)

while True:
	randStockId = random.randint(0,nasdaqLength)
	pickedStock = nasdaqRows[randStockId][0]
	print("Getting Stock Data")
	profileData = validateStock(pickedStock)
	if profileData == None:
		print("Failed, trying again")
		continue
	else:
		print("Success, now posting to Twitter")
		stock_tweet = generateTweet(profileData)
		api.update_status(stock_tweet)
		time.sleep(INTERVAL)