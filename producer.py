from twitter_manager import TwitterManager

tm = TwitterManager(stream='kafka', topic='tweets')
tm.myStream.filter(track=['Chicago'])


