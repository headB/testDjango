from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    #return HttpResponse("Hello world !I am kumanxuan!! ")
    return render(request,'test.html')