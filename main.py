from tweetsearcher import TweetSearcher


def simple():
    searcher = TweetSearcher()
    tweets, cursor = searcher.get_tweets('trump', since='2017-01-01', until='2018-01-01', max_tweets=200)
    print(tweets, cursor)


def proxy():
    searcher = TweetSearcher(proxy='socks5h://51.15.100.63:1080')
    tweets, cursor = searcher.get_tweets('trump', since='2017-01-01', until='2018-01-01', max_tweets=200)
    print(tweets, cursor)


def save_to_file():
    searcher = TweetSearcher()
    tweets, cursor = searcher.tweets_to_csv('trump', since='2017-01-01', until='2018-01-01', max_tweets=200)
    print(tweets, cursor)


if __name__ == '__main__':
    # simple()

    proxy()

    # save_to_file()
