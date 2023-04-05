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

def index(request):
    objs = Article.objects.all()
    context = {
        'title':'Utaite Site',
        'articles':objs,
    }
    return render(request, 'mysite/index.html', context)

