from django.shortcuts import render
from django.http import HttpResponse
import json
from requests_oauthlib import OAuth1Session
from blog.models import Article
from django.shortcuts import render
# from django.shortcuts import redirect
#--独自モジュール--------------------------------------
# from twitter.modules import security
from mysite.modules import tweepy
#--メッセージ------------------------------------------
# from django.contrib import messages
#--ログツール------------------------------------------
import logging
import pandas as pd
#logging.debug('hi_debug')

# consumer_key = '91yx7Z1PzJVyL6PUqv5EwLlFU'
# consumer_secret= 'ZTW5QFjnEdCSw8PSZvEuBQVCVveIg4OfTl641LHvRAhgwNnd0Z'
# access_token    = '1376917526316085253-7RN39UcFSRsVT10yYtw5mchPxNGitF'
# access_secret  = 'JdnoJNUT3Mu7C8ANe7jvtyYZt4TcnfXHcW34eJ7qXXcnR'

# oauth_session_params = {
#     'consumer_key':'91yx7Z1PzJVyL6PUqv5EwLlFU',
#     'consumer_secret':'ZTW5QFjnEdCSw8PSZvEuBQVCVveIg4OfTl641LHvRAhgwNnd0Z',
#     'access_token' : '1376917526316085253-7RN39UcFSRsVT10yYtw5mchPxNGitF',
#     'access_secret':'JdnoJNUT3Mu7C8ANe7jvtyYZt4TcnfXHcW34eJ7qXXcnR',
# }

# twitter = OAuth1Session(
#     oauth_session_params['consumer_key'],
#     oauth_session_params['consumer_secret'],
#     oauth_session_params['access_token'],
#     oauth_session_params['access_secret']
#     )

# url = "https://api.twitter.com/1.1/search/tweets.json?"
# params={
#     'q':'#歌ってみた',
#     'count': 2,
# }
# res=twitter.get(url,params=params)

# print(res.text)

# tweets = 100

def index(request):
    objs = Article.objects.all()
    context = {
        'title':'Utaite Site',
        'articles':objs,
    }
    return render(request, 'mysite/index.html', context)

