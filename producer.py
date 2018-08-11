from twitter_manager import TwitterManager

tm = TwitterManager(stream='kafka', topic='tweets')
tm.myStream.filter(track=['Chicago'])

# Streaming
#tm.myStream.filter(track=['Chicago'])

# REST Api 
public_tweets = tm.api.search('from:elonmusk', count=20)
for tweet in public_tweets:
    print(tweet.text)
