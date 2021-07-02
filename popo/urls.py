from django.urls import path

from popo.views import hello_world

app_name = 'popo'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]

# urlpatterns = [
#     path('hi/', hi, name='hi')
# ]