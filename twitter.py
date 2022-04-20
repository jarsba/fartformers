import tweepy
import pandas as pd
import csv
import re
import string
import os
from dotenv import load_dotenv
from string import printable

load_dotenv()


def filter_tweet(text):



    if "@" in text:
        return False

    if "RT" in text[0:2]:
        return False

    if "http:" in text or "https:" in text:
        return False

    text = ''.join(filter(lambda x: x in printable, text))

    if len(text) < 25:
        return False

    return True


class CSVTweetStreamer(tweepy.StreamingClient):

    def __init__(self, bearer_token, csv_file, csv_writer, **kwargs):
        super().__init__(bearer_token, **kwargs)
        self.rows = 0
        self.csv_file = csv_file
        self.csv_writer = csv_writer

    def on_tweet(self, tweet):
        if self.rows > 10000:
            self.disconnect()
            self.csv_file.close()

        if tweet.lang == "en" and filter_tweet(tweet.text):
            print(tweet.text)
            print(tweet.lang)
            self.csv_writer.writerow([tweet.id, tweet.text, tweet.lang])
            self.rows += 1


def write_topics():
    topics = open('topics.csv', 'w')
    csv_writer = csv.writer(topics)

    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    csv_tweeter = CSVTweetStreamer(bearer_token, topics, csv_writer)
    csv_tweeter.sample(tweet_fields=["id", "text", "lang"])

if __name__ == '__main__':
    write_topics()
