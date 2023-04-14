from django.db import models

# Create your models here.
class Music(models.Model):
    # 앨범 커버 이미지
    image = models.ImageField()
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

