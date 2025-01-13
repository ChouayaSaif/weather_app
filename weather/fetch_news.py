import requests

import feedparser

feed_url = "https://weather.com/news/rss"

def fetch_weather_rss(feed_url):
    feed = feedparser.parse(feed_url)
    return [{"title": entry.title, "link": entry.link} for entry in feed.entries]
