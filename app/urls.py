from django.http import HttpResponse
from django.urls import path

def top(request):
    return HttpResponse('top page')

urlpatterns = [
    path('', top),
]