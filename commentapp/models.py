from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):

    # 게시글   // ForeignKey : 1대 다 처럼 여러 사람이 댓글을 남길 수 있음
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
        # article = 게시글이 삭제되었3을때 없는 것처럼 함

    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)

    content = models.TextField(null=False)
        # 장문의 길이를 쓸 시 Textfield

    create_at = models.DateTimeField(auto_now_add=True)
        # DateTimeField : 날짜와 시간까지 출력
        # auto_now_add=True : 서버에서 굳이 지정안해도 자동으로 시간이 나옴


