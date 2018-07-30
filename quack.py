import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.text)

tweets = api.user_timeline()
for tweet in tweets:
    print(tweet.text)
