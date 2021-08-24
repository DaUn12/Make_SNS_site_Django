from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like_record', null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record', null=True)

    class Meta:             # 외부데이터 = 메타데이터  (장고에서만 가능 )
        unique_together = ['user', 'article']


