# tweet-searcher
Library to bypass limitations of the Twitter Official API

Inspired by https://github.com/Jefferson-Henrique/GetOldTweets-python

# Instalation

```
pip install tweetsearcher
```

# Usage
Simple download 200 on the search query "trump" since 2017-01-01 and until 2018-01-01:

```python
from tweetsearcher import TweetSearcher
searcher = TweetSearcher()
tweets, cursor = searcher.get_tweets('trump', since='2017-01-01', until='2018-01-01', max_tweets=200)
print(tweets, cursor)
```

If you want to save tweets to csv:

```python
from tweetsearcher import TweetSearcher
searcher = TweetSearcher()
tweets, cursor = searcher.tweets_to_csv('trump', since='2017-01-01', until='2018-01-01', max_tweets=200)
print(tweets, cursor)
```

With proxy:

```python
from tweetsearcher import TweetSearcher
searcher = TweetSearcher(proxy='socks5h://60.50.251.54:8181')
tweets, cursor = searcher.tweets_to_csv('trump', since='2017-01-01', until='2018-01-01', max_tweets=200)
print(tweets, cursor)
```

Custom headers:

```python
searcher = TweetSearcher(headers={
    'Host': "twitter.com",
    'User-Agent': 'Chrome/66.0.3359.181',
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Language': "de,en-US;q=0.7,en;q=0.3",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive"
})
```

To prevent the ban after downloading each page, the process sleeps for a while:

```python
searcher = TweetSearcher(delay_min=1, delay_max=3)
```


