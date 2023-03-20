from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexview(request):
    if request.method == 'GET':
        return HttpResponse('indexview get func')
    else:
        return HttpResponse('indexview post func')



