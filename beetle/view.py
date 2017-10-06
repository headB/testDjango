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

    #admin = Admin(name='kumanxuan',detail='666',description='No why!')
    #admin.save()
    #成功向数据库插入数据，现在插上提取数据。
    res = Admin.objects.all()

    listName = []
    listDescription = []

    #print(res.item())

    for x in res:
        #pass
     #for y in range(0,2):
        listName.append(x.name)
        listDescription.append(x.description)
    #methodC['dbInfo'] = res

    #当循环储存好数值之后，就把列表的数值赋值给字典。
    methodC['name'] = listName
    methodC['description'] = listDescription
    print(methodC)
    return render(request,'test.html',methodC)

##哦哦，原来这个地方的VIEW是相当于php里面的MVC结构里面的Controller啦。
def TestModelSql(request):
    pass