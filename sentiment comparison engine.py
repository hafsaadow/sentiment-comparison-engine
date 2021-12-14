import tweepy
import preprocessor as p
from textblob import TextBlob
import statistics
from typing import list
from secret import consumer_key, consumer_secret

def get_tweets(keyword: str) -> list[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').item(10):
        all_tweets.append(tweet.full_text)
    return all_tweets


def clean_tweets(all_tweets: list[str]) -> list[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))

    return tweets_clean

def get_sentiment(all_tweets: list[str]) -> list[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_average_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)

    average_score = statistics.mean(sentiment_scores)
    return average_score



if __name__ == "__main__":
    print("Who do you prefer?")
    first_thing = input()
    print("...or...")
    second_thing = input()
    print("\n")

    first_score = generate_average_sentiment_score(first_thing)
    second_score = generate_average_sentiment_score(second_thing)

    if (first_score > second_score):
        print("People prefer {first_thing} over {second_thing}")
    else:
        print("People prefer {second_thing} over {first_thing}")

