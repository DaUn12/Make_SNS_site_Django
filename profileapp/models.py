from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,
                                related_name='profile')
    # OneToOneField :  accountapp 과 1대 1로 작성
    #   User : 유저 클래스를 상속받음
    # on_delete :  계정이 탈퇴 시 삭제가 될 시 어떻게생성할 시
    # CASCADE  : (종속), 계정이 탈퇴시 프로파일도 자동 삭제가 되도록 함
    # related_name : use 객체에서 profile 으로 접근을 할때 어떤이름으로 접근할지지


    image = models.ImageField(upload_to='profile/', null=True)
    # upload_ to : 이미지를 다운받았을때의 저장하는 경로
    # (profile 이라는 파일로 저장되고 그안에 이미지를 다운시킴)
    # null : 이미지가 비어있어도 상관이 없음

    nickname = models.CharField(max_length=30, unique=True, null=True)
    # unique : 중복되는 닉네임이 없도록 설정

    message = models.CharField(max_length=200, null=True)
