from django.db import models

# 30강
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    # on_delete : 유저 삭제시 취할 행동, CASCADE: 유저 삭제시 프로파일 같이 삭제
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    massage = models.CharField(max_length=100, null=True)