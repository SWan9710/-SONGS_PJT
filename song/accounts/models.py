from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # follow 모델 설정
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
