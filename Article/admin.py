from django.contrib import admin

from .models import Article

# Register your models here.

class ArticleManager(admin.ModelAdmin):
    list_display=('title','slug','published','created','updated','status')
    list_filter=('published','status')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}

admin.site.register(Article,ArticleManager)