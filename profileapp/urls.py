from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
# 로직을 트리거할 주소


    path('create/', ProfileCreateView.as_view(), name='create'),
]
