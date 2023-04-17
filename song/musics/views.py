from django.shortcuts import render, redirect
from .models import Music, Comment
from .forms import MusicForm, CommentForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    return render(request, 'musics/index.html', context)

@require_http_methods(['GET'])
def detail(request, pk):
    music = Music.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = music.comment_set.all()
    context = {
        'music' : music,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'musics/detail.html', context)

@require_http_methods(['POST','GET'])
def create(request):
    if request.method =='POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            return redirect('musics:detail', music.pk) 
    else:
        form = MusicForm()
    context = {'form':form}
    return render(request, 'musics/create.html', context)

@require_http_methods(['POST','GET'])
def update(request, pk):
    music = Music.objects.get(pk=pk)
    if request.user == music.user:
        if request.method =='POST':
            form = MusicForm(request.POST, request.FILES, instance = music)
            if form.is_valid():
                music.save()
                return redirect('musics:detail', pk=music.pk)
        else:
            form = MusicForm(instance=music)
    else:
        return redirect('musics:detail', music.pk)
    context = {'form':form, 'music':music}
    return render(request, 'musics/update.html', context)

@require_http_methods(['POST'])
def delete(request, pk):
    music = Music.objects.get(pk=pk)
    if request.user == music.user:
        music.delete()
        return redirect('musics:index')
    return redirect('musics:detail', music.pk)

@require_http_methods(['POST'])
def comments_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    music = Music.objects.get(pk = pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.music = music
        comment.user = request.user
        comment.save()
    return redirect('musics:detail', music.pk)

@require_http_methods(['POST'])
def comments_delete(request, pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('musics:detail', pk)

@require_http_methods(['POST'])
def likes(request, music_pk):
    if request.user.is_authenticated:
        music = Music.objects.get(pk=music_pk)
        if music.like_users.filter(pk=request.user.pk).exists():
            music.like_users.remove(request.user)
        else:
            music.like_users.add(request.user)
        return redirect('musics:index')
    return redirect('accounts:login')