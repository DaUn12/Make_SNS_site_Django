from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import DetailView

from popo.views import hello_world, AccountCreateView, AccountDetailView

app_name = 'popo'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    #path ( 라우팅할 경로, 함수이름(클래스 시 : 클래스.as_view), 사용할 이름)
    # 어떤 url 로 가야 회원가입 로직으로 가는지


    path('login/', LoginView.as_view(template_name= 'accountapp/login.html'),   # 경로
                                     name='login'),
# templates앱 네임이 accountapp 인걸로 가서 url이 hello_world 로 가라
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail')
]




# urlpatterns = [
#     path('hi/', hi, name='hi')
# ]