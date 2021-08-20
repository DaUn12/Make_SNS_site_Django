from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name='subscription', null=False)
     # 사용자는 null 값이 없어야 하기 때문에 null = False

    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)
    # created_at : 언제 구독을 했는지

    class Meta:         # Meta :외적인데이터의 정보
        unique_together = ['user', 'project']
            # 유일하게 두개의 정보를 유니크하게 나타남
            # form을 안눌러도됨 !!
