from django.contrib import admin

from .models import Article,Catagory

# Register your models here.

class CatagoryManager(admin.ModelAdmin):
    list_display=('slug','status')
    list_filter=(['status'])
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}

class ArticleManager(admin.ModelAdmin):
    list_display=('title','slug','published','created','updated','status','catagory_to_str')
    list_filter=('status',)
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}

    def catagory_to_str(self,obj):
        return ",".join([catagory.title for catagory in obj.cataogry.all()])

admin.site.register(Article,ArticleManager)
admin.site.register(Catagory,CatagoryManager)