from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request,'bbase.html')


# def hi(request):
#     return HttpResponse('Hello !!')