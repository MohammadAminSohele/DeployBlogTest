from django.shortcuts import render

from .models import Article

# Create your views here.

def article_detail(request,slug):
    context={
        'article':Article.objects.get(slug=slug)
    }
    return render(request,'detail.html',context)