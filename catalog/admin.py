from django.contrib import admin
from catalog.models import Article, ArticleBias

# Register articles in admin site.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

# Register article bias entries in admin site.
@admin.register(ArticleBias)
class ArticleBiasAdmin(admin.ModelAdmin):
    list_display = ('reader', 'bias', 'article', 'used')
    list_filter = ('used',)
