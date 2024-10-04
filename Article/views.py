from django.shortcuts import render,get_object_or_404

from Article.models import Article

# Create your views here.

def home(request):
    context={
        'Slider':Article.objects.order_by('-created').all()[:1],
        'Article':Article.objects.filter(status='p').order_by('created'),
    }
    return render(request,'home.html',context)

def article_detail(request,slug):
    context={
        'article':get_object_or_404(Article,slug=slug,status='p')
    }
    return render(request,'detail.html',context)