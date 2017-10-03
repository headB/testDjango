from django.http import HttpResponse
from django.shortcuts import render
from testModel.models import Admin

def hello(request):

    #return HttpResponse("Hello world !I am kumanxuan!! ")

    #return render(request,'test.html')
    methodC = {}
    if (request.method=='GET'):
        methodC['method']='这个是一一个Get处理方法'
    else:
        methodC['method']='这个是一一个Post处理方法'

    admin = Admin(name='kumanxuan',detail='666',description='No why!')
    admin.save()

    return render(request,'test.html',methodC)

##哦哦，原来这个地方的VIEW是相当于php里面的MVC结构里面的Controller啦。
def TestModelSql(request):
    pass