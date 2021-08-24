from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
        # 1대 다로 테이블과 테이블을 연결함  ,,, User 을 연결
        # on_delete : user 가 삭제 되었을 떄 하는 것
        # null 값도 ok 하다는 것임

    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image =models.ImageField(upload_to='article/', null=True)
    # media 파일 안에 article 이라는 폴더가 생기고 그 안에 사진이 자동으로 업로드됨

    content = models.TextField(null=True)
    #  TextField: 장문을 이용 시 사용

    created_at = models.DateField(auto_now_add=True, null=True)
    # DateField : 언제작성했는지 알 수 있음
    # auto_now_add : 자동으로 시간을 작성해줌줌

    like = models.IntegerField(default=0)