# twitter-kafka
Stream Twitter data into Kafka

## Producer.py

Instantiates the TwitterManager. If stream='console' then the StreamListener will print tweets to the console.
If stream='kafka' and a topic name is provided, then the StreamListener on_status is overriden to send publish the Tweets to a Kafka topic.


To start streaming we can call.

## Twitter_Manager.py

Class to connect to Twitter.

The `api` attribute the TwitterManager is the point of entry to Twitter REST API.
This code will search and return the 20 most recent tweets that contain the word Chicago.

```
tm = TwitterManager()

public_tweets = tm.api.search('Chicago', count=20)
for tweet in public_tweets:
    print(tweet.text)
```

The `myStream` attribute of the TwitterManager is the point of entry to Twitter Streaming API.
This code will start streaming all tweets that contain the word 'Chicago' and print them to the console.

```
tm = TwitterManager(stream='console')

tm.myStream.filter(track=['Chicago'])
```