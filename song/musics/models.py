from django.db import models
from django.conf import settings

# Create your models here.
class Music(models.Model):
    # 앨범 커버 이미지
    image = models.ImageField(blank=True)
    # 노래 제목
    title = models.CharField(max_length=20)
    # 가수명
    artist = models.CharField(max_length=20)
    # 노래 설명
    description = models.TextField()
    # 장르별
    genre = models.CharField(max_length=30)
    # 날씨별
    weather = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_musics')

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)