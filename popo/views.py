from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request,'accountapp/hello_world.html')


# accountapp = popo 라고 보자 하고 그 안에 hello_world를 넣는 것 #}

# def hi(request):
#     return HttpResponse('Hello !!')