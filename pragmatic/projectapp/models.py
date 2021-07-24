from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    description = models.TextField(null=True)
    
    created_at = models.DateField(auto_now_add=True, null=True)
    
    # article 생성 시 Project 순번, 이름 보이도록
    def __str__(self):
        return f'{self.pk} : {self.title}'