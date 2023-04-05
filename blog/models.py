from django.db import models

# Create your models here.
class Article(models.Model):
    tweet_id = models.CharField(verbose_name='ツイートID', max_length=100,)

    name = models.CharField(verbose_name='名前', max_length=100, blank=True, null=True)

    user_id = models.CharField(verbose_name='ユーザーID', max_length=100, blank=True, null=True)
    
    screen_name = models.CharField(verbose_name='ユーザーネーム', max_length=100, blank=True, null=True)
    
    text = models.TextField(verbose_name='ツイート文', blank=True, null=True)
    
    url = models.URLField(default="", blank=True, null=True)
    
    html = models.TextField(verbose_name='埋め込みコード',)

    created_at = models.DateField(auto_now_add=True)

    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = '歌い手'
        verbose_name_plural = '歌い手リスト'