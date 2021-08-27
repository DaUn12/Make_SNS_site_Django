"""homepa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articleapp.views import ArticleListView

urlpatterns = [
    # 아무것도 경로를 안줬을 시
    path('', ArticleListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
# 장고가 기본적으로 준 주소 (관리자 페이지)
    path('accountss/', include('popo.urls')),
#path = 장고에서 제공하는 기능 , 경로를 accounts
    path('profiles/', include('profileapp.urls')),
    # profiles 로가는 겨올를 설정
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('likes/', include('likeapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path(내가만들 경로 이름, include(include(appname.url))