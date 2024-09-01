from django.shortcuts import render,get_object_or_404

from Article.models import Article,Catagory

# Create your views here.

# def home(request):
#     Slider=Article.objects.order_by('-created').all()[:1]
#     context={
#         # region ValueList
#         # 'articles':[
#         #     {
#         #         'title':'title1',
#         #         'description':'description 1'
#         #     },
#         #      {
#         #         'title':'title2',
#         #         'description':'description 2'
#         #     }
#         # ]
#         # endregion

#         'title':'Home page',
#         'Slider':Slider,
#         'Article':Article.objects.filter(status='p').order_by('created'),
#         'Catagory':Catagory.objects.filter(status=True)
#     }
#     return render(request,'home.html',context)

def article_detail(request,slug):
    context={
        'article':get_object_or_404(Article,slug=slug,status='p')
    }
    return render(request,'detail.html',context)