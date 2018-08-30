from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

import tweepy
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweet_archive = []
channels = {}

following = []
user_prefs = {}

for friend in tweepy.Cursor(api.friends).items():
    following.append(json.loads(friend._json))

# def build_channel(channel_name, channel_criteria):
#     channels[channel_name] = channel_criteria

# def populate_channels(tweet):
#     for channel, criteria in channels.items():
#         for criterion, filters in criteria.items():
#             for each filt in filters:
#                 if criterion == 'text':
#                     if filt in tweet['text']:
#                         channel


# def parse_tweet(status):
#     tweet = json.loads(status)
#     return tweet


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet_archive.append(parse_tweet(status))

# build_channel("dog media",{'text':["dog","puppy"],'hashtags':['#dog','puppies'],'entities':['media']})

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(filter_level=['medium'],follow=following)
