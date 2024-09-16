from django.http import HttpResponse
from django.http import JsonResponse

def home_HttpResponse(request):
    return HttpResponse('hello world')

def home_Json(request):
    data={
        'title':'title',
        'description':'description',
        'age':19
    }
    return JsonResponse(data)

