from django.shortcuts import render
from .models import Music

# Create your views here.
def index(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    return render(request, 'musics/index.html', context)