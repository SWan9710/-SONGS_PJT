from django import forms
from .models import Music, Comment

music_genre = [('전체', '전체'), ('발라드','발라드'), ('댄스', '댄스'), ('힙합','힙합'), ('재즈','재즈')]

music_weather = [('전체', '전체'), ('화창', '화창'), ('흐림', '흐림'), ('비', '비')]

# 뮤직폼 작성 - 장르와 날씨는 ChoiceField 사용
class MusicForm(forms.ModelForm):
    genre = forms.ChoiceField(
        choices = music_genre,
    )

    weather = forms.ChoiceField(
        choices = music_weather
    )

    class Meta:
        model = Music
        exclude = (
            'user',
            'like_users',
        )
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            'music',
            'user',
        )