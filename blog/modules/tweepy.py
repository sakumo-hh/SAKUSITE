
#--twitter読み込み-------------------------------------
import json
from requests_oauthlib import OAuth1Session
#--ログツール------------------------------------------
import logging
import pandas as pd
#logging.debug('hi_debug')

class TwitterApi:
    def __init__(self, oauth_session_params):
        CONSUMER_KEY    = oauth_session_params['consumer_key']
        CONSUMER_SECRET = oauth_session_params['consumer_secret']
        ACCESS_TOKEN    = oauth_session_params['access_token']
        ACCESS_SECRET   = oauth_session_params['access_secret']
        self.twitter    = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        self.url_trend  = "https://api.twitter.com/1.1/trends/place.json"
        self.url_search = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"
        self.url_embed  = "https://publish.twitter.com/oembed"
        self.url_status = "https://api.twitter.com/1.1/statuses/show.json"

    def search_tweets(self, keyword, count):
        params = {'q': keyword, 'count': count,'result_type': 'recent',}
        request = self.twitter.get(self.url_search, params = params)
        if request.status_code == 200:
            result = json.loads(request.text)
            return result

    def get_tweet_ids(self, result):
        global tweet_ids
        tweet_ids = []
        for tweet in result['statuses']:
            if not len(tweet['entities']['urls']) <= 0:
        	    tweet_ids.append(str(tweet['id']))
        return tweet_ids

    def get_screen_names(self, tweet_ids):
        global screen_name
        embed_params_dicts = []
        for tweet_id in tweet_ids:
            params = {'id': tweet_id}
            request = self.twitter.get(self.url_status, params = params)
            status = json.loads(request.text)
            user_name = status['user']['name']
            user_id = status['user']['id']
            screen_name = status['user']['screen_name']
            text = status['text']
            url = status['user']['url']
            embed_params_dict = dict(tweet_id=tweet_id,name=user_name,user_id=user_id,screen_name=screen_name,text=text,url=url) 
            embed_params_dicts.append(embed_params_dict)
        # df=pd.DataFrame(embed_params_dicts)
        # # df.to_csv("employee.csv",encoding="utf_8_sig")
        # df['new_col']= 0
        return embed_params_dicts
    
    def get_embed_datas(self, embed_params_dicts):
        embed_datas = []
        # tweets_datas = []
        for e in embed_params_dicts:
            url = 'https://twitter.com/'+e['screen_name']+'/'+'status/'+e['tweet_id']
            params = {'url': url, 'hide_media': False, 'hide_thread': True, 'lang': 'ja', 'align': 'center', 'theme': 'dark', 'maxwidth': 300,}
            request = self.twitter.get(self.url_embed, params = params)
            embed_data = json.loads(request.text)
            embed_datas.append(embed_data['html'])
            # data = dict(html_code=embed_datas)
            # tweets_datas.append(data)
        # tweet_id = embed_params_dicts[0:] 
        # screen_name  = embed_params_dicts[1:]
        # ziplist=list(zip(embed_params_dicts,embed_datas))
        # embed_params_dicts.append(embed_datas)
        df=pd.DataFrame(embed_params_dicts)
        # df['new_col']= 0
        s=pd.DataFrame(embed_datas)
        df.insert(len(df.columns), 'html', s)
        df.to_csv("employee.csv",encoding="utf_8_sig",mode='a',index=False)
        dd=pd.read_csv("employee.csv")
        data = dd.drop_duplicates(subset=['tweet_id'], keep=False)
        data.to_csv("employee.csv",encoding="utf_8_sig",index=False)
        return embed_datas

    def get_tweets(self, keyword, count):
        result             = self.search_tweets(keyword, count)
        tweet_ids          = self.get_tweet_ids(result)
        embed_params_dicts = self.get_screen_names(tweet_ids)
        embed_datas        = self.get_embed_datas(embed_params_dicts)
        return embed_datas


# embed_params_dict['tweet_id'] = tweet_id
    # embed_params_dict['screen_name'] = screen_name
    # df=pd.DataFrame(list1)
    # df.to_csv('tweet.csv',index=True)
    # d=dict(tweet_id=tweet_id,screen_name=screen_name)
    # df=pd.DataFrame(data=d)
    # df.to_csv('tweet.csv',index=True)
    # embed_params_dicts.append(dict)
    # list1=(screen_name)
    # df=pd.DataFrame(list1)
    # df.to_csv('tweet.csv',index=True)
    
    # df=pd.DataFrame(embed_params_dicts)
    # df.to_csv('tweet.csv',index=True)


    # print(get_screen_names(tweet_ids))
    
    # df=pd.DataFrame(data=x)
    # # CSV ファイル (employee.csv) として出力 
    # df.to_csv("employee.csv")

    # def get_csv(self, embed_params_dicts):
    # embed_params_dicts = x
    # df=pd.DataFrame(data=embed_params_dicts)
    # df.to_csv('tweet.csv',index=True)


# # api_key       = "91yx7Z1PzJVyL6PUqv5EwLlFU"
# # api_secret    = "ZTW5QFjnEdCSw8PSZvEuBQVCVveIg4OfTl641LHvRAhgwNnd0Z"
# # access_key    = "1376917526316085253-7RN39UcFSRsVT10yYtw5mchPxNGitF"
# # access_secret = "JdnoJNUT3Mu7C8ANe7jvtyYZt4TcnfXHcW34eJ7qXXcnR"

# # auth = tweepy.OAuth1UserHandler(api_key, api_secret)
# # auth.set_access_token(access_key, access_secret)
# # api = tweepy.API(auth)


# # def get_tweets(search, num):
    
# #     # API連携してツイート情報を収集
# #     tweets = tweepy.Cursor(api.search_tweets,q=search,).items(num)

# #     # 取得した情報から必要なものをリストに格納
# #     tweets = list(tweets)
# #     tweet_data = []
# #     for tweet in tweets:
# #         tweet_data.append([tweet.id, tweet.user.id, tweet.user.name, tweet.text, tweet.favorite_count, tweet.retweet_count, tweet.created_at])

# #     return tweet_data