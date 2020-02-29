import tweepy
import time

auth = tweepy.OAuthHandler('2RCccFocYRev9NJBFYG75FWBI', 'W6LkYONDIcvtmXtQibxVvDacKihwEkDPd5ONqLV9RoSvEoxLi7')
auth.set_access_token('1231327904392470529-GdJRoUL0mRnVoWxhH1fT0SrLc8yxlt', 'VlLZ5YAc6MDLVbrjYOQA1RGoJCnjiv3TAtc9qvPaDhAl8')

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

api = tweepy.API(auth)
user=api.me()

def limit_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimiteError:
		time.sleep(1000) # 1 second

# Follows back
#for follower in limit_handler(tweepy.Cursor(api.followers).items()): # Loop through followers
	#if follwer.name == 'name':
		#follower.follow() follows user
	
	#print(follower.name)

#If tweet contains 'python', will like tweet
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break