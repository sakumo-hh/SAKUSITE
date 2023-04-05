from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json
from requests_oauthlib import OAuth1Session
from blog.models import Article
# from django.shortcuts import redirect
#--独自モジュール--------------------------------------
# from twitter.modules import security
from blog.modules import tweepy
#--メッセージ------------------------------------------
# from django.contrib import messages
#--ログツール------------------------------------------
import logging
import pandas as pd
from django.conf import settings

# Create your views here.
def article(request,pk):
    obj = Article.objects.get(id=pk)
    context={
        'article':obj,
    }
    return render(request, 'blog/article.html', context)

def blog(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        count   = request.POST['count']
        oauth_session_params = {}
        oauth_session_params['consumer_key']    = settings.TWEET_CONSUMER_KEY
        oauth_session_params['consumer_secret'] = settings.TWEET_CONSUMER_SECRET
        oauth_session_params['access_token']    = settings.TWEET_ACCESS_TOKEN
        oauth_session_params['access_secret']   = settings.TWEET_ACCESS_SECRET
                    #--------------------------------------
        twitterApi = tweepy.TwitterApi(oauth_session_params)
        tweets = twitterApi.get_tweets(keyword, count)
    else:
        keyword = '#歌ってみた #歌い手さんMIX師さん絵師さん動画師さんPさんと繋がりたい filter:videos filter:links min_faves:50 exclude:replies exclude:retweets '
        count   = 10
        tweets  = ''

    context = {
        'keyword': keyword,
        'count'  : count,
        'tweets' : tweets,
    }
    return render(request, 'blog/search.html', context)
