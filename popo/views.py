from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from popo.models import NewModel


def hello_world(request):

    if request.method =='POST':

        if request.method == 'POST':
            temp = request.POST.get('input_text')
            new_model = NewModel()
            new_model.text = temp
            new_model.save()


            return render(request,'accountapp/hello_world.html'
                      ,context={'new_model': new_model})


    else:
        return render(request,'accountapp/hello_world.html'
                      , context={'text': 'POST GET!'})

# accountapp = popo 라고 보자 하고 그 안에 hello_world를 넣는 것 #}

# def hi(request):
#     return HttpResponse('Hello !!')