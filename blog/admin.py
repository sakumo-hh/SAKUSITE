from django.contrib import admin
from django.contrib import admin
from .models import Article  
from import_export import resources  
from import_export.admin import ImportExportModelAdmin  
from import_export.fields import Field 

class ArticleResource(resources.ModelResource):
   # field名とcsvの列名が異なる場合はここで指定する。
   # ここでは、postalcode / postalCode、category / categoriesと微妙に異なる。   
   # django-import-exportのModel設定
   class Meta:
       model = Article
       # Controls if the import should skip unchanged records. Default value is False
       skip_unchanged = True
       use_bulk = True

@admin.register(Article)
# ImportExportModelAdminを継承したAdminクラスを作成する
class ArticleAdmin(ImportExportModelAdmin):
   ordering = ['id']
   list_display = ('id', 'tweet_id', 'name', 'user_id', 'screen_name', 'text','url','html')
   # resource_classにModelResourceを継承したクラス設定
   resource_class = ArticleResource