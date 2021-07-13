from django.urls import path

from popo.views import hello_world, AccountCreateView

app_name = 'popo'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create')
    #path ( 라우팅할 경로, 함수이름(클래스 시 : 클래스.as_view), 사용할 이름)

]
# 앱 네임이 accountapp 인걸로 가서 url이 hello_world 로 가라



# urlpatterns = [
#     path('hi/', hi, name='hi')
# ]