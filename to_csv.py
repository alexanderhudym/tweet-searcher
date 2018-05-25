import sys
from getopt import getopt
from tweetsearcher import TweetSearcher

if __name__ == '__main__':
    try:
        opts, args = getopt(sys.argv[1:], '', ('q=', 'since=', 'until=', 'username=', 'max_tweets=', 'file_name=',
                                               'lang=', 'proxy=', 'delay_min=', 'delay_max=', 'cursor='))
        q = ''
        since = ''
        until = ''
        username = ''
        max_tweets = 0
        file_name = ''
        lang = ''
        proxy = ''
        delay_min = 0
        delay_max = 2
        cursor = ''

        for opt, arg in opts:
            if opt == '--q':
                q = arg
            elif opt == '--since':
                since = arg
            elif opt == '--until':
                until = arg
            elif opt == '--username':
                username = arg
            elif opt == '--max_tweets':
                max_tweets = int(arg)
            elif opt == '--file_name':
                file_name = arg
            elif opt == '--lang':
                lang = arg
            elif opt == '--proxy':
                proxy = arg
            elif opt == '--delay_min':
                delay_min = int(arg)
            elif opt == '--delay_max':
                delay_max = int(arg)
            elif opt == '--cursor':
                cursor = arg

        searcher = TweetSearcher(proxy=proxy, delay_min=delay_min, delay_max=delay_max)
        searcher.tweets_to_csv(q, since, until, max_tweets=max_tweets, username=username, lang=lang,
                               file_name=file_name, cursor=cursor)
    except Exception as err:
        print(err)