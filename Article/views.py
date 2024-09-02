from django.shortcuts import render,get_object_or_404

from Article.models import Article,Catagory

# Create your views here.

def article_detail(request,slug):
    context={
        'article':get_object_or_404(Article,slug=slug,status='p')
    }
    return render(request,'detail.html',context)