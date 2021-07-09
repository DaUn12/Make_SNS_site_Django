from django.db import models

# Create your models here.
class NewModel(models.Model):
    text = models.CharField(max_length=255, null = False)
    # charfield : 문자열 받음 ,max_length : 최대 문자열 255, null = 공란의 여부
