from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from Article.models import Article

def home_HttpResponse(request):
    return HttpResponse('hello world')

def home(request):
    Slider=Article.objects.order_by('-created').all()[:1]
    print(Slider)
    context={
        # region ValueList
        # 'articles':[
        #     {
        #         'title':'title1',
        #         'description':'description 1'
        #     },
        #      {
        #         'title':'title2',
        #         'description':'description 2'
        #     }
        # ]
        # endregion

        'title':'Home page',
        'Slider':Slider,
        'Article':Article.objects.filter(status='p').order_by('created'),
    }
    return render(request,'home.html',context)

def home_Json(request):
    data={
        'title':'title',
        'description':'description',
        'age':19
    }
    return JsonResponse(data)

