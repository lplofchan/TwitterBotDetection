#!/usr/local/bin/python

# Leah Plofchan, Erin Flynn, Brynna Conway
# Social Sensing and Cyber Physical Systems Final Project
# Twitter Bot Detector Class

import tweepy, sys

class BotDetector():
	def __init__(self, api):
		self.api = api
			
	def find_ratio(self, userID):
		# find ratio of followers/following
		user = self.api.get_user(userID)
		print user.screen_name
		followers = len(self.api.followers_ids(userID))
		friends = len(self.api.friends_ids(userID))
		print followers
		print friends
		return float((float(followers)/float(friends)))

		# activity level of user -- how often it tweets and how much it likes other tweets
	# analyze screenname of user and bio
	# score function
	def num_tweets(self, userID):
		status = self.api.user_timeline(user_id = userID, include_rts = True, count = 200)
		print "in here"
		count = 0
		for tweet in status:
			count += 1
			print tweet.text.encode('utf-8')
		print count
	
if __name__ == "__main__":
	# set up authentication
	auth = tweepy.OAuthHandler('OQvy6pyogx5mxHoIHIHXIIOZh', 'CSXM1Z3UYctTmf4DNL0TtPUD4ecE1AOVc4gJPuSsBYUY8mYnIl')
	auth.set_access_token('3083135683-DER2kEd9yhEbf7qY2q58haf6MJE3yTzXlOaw9rJ', 	'lU8PL9RrGpmhaxqxmasWP6wzYBMHfB1fOw0TZYe71A380')

	# call tweepy API
	api = tweepy.API(auth)
	
	userID = '965192514'
	bd = BotDetector(api)
	print(bd.find_ratio(userID))

	bd.num_tweets(userID)
		
		
		
		
		