import tweepy
from confluent_kafka import Producer
import socket
import config as CONFIG

class TwitterManager:
    def __init__(self, stream=None, topic=None):
        self.auth = tweepy.OAuthHandler(CONFIG.CONSUMER_KEY, CONFIG.CONSUMER_SECRET)
        self.auth.set_access_token(CONFIG.ACCESS_TOKEN, CONFIG.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)
        self.myStream = self._set_stream(stream, topic)

    def _set_stream(self, stream, topic=None):
        if stream:
            if stream == 'console':
                return tweepy.Stream(auth=self.auth, listener=ConsoleOutput())
            elif stream == 'kafka':
                if topic:
                    return tweepy.Stream(auth=self.auth, listener=TweetProducer(topic))
                else:
                    raise Exception('A topic name is needed when using Kafka Streaming')
            else:
                raise Exception('Only "console" or "kafka" stream are allowed.')

class ConsoleOutput(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

class TweetProducer(tweepy.StreamListener):
    def __init__(self, topic):
        super().__init__()
        conf = {'bootstrap.servers': "localhost:9092",
                'client.id': socket.gethostname(),
                'default.topic.config': {'acks': 'all'}}
        self.topic = topic
        self.producer = Producer(conf)

    def on_status(self, status):
        message = status.text.encode('utf-8')
        try:
            self.producer.produce(self.topic, message)
        except Exception as e:
            print(e)
            # Needed to stop stream and close connection.
            return False
        return True