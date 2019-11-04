from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article
from .forms import CreateArticle


def get_article_list(request):
    articles = Article.objects.all().order_by('title')
    return render(request, 'articleusers/articles_list.html', {'articles': articles})

@login_required(login_url='/users/login')
def put_article(request, articleid):
    if request.method == 'POST':
        form = CreateArticle(request.POST)
        if form.is_valid():
            article = get_object_or_404(Article.objects.all(), author=request.user,pk=int(articleid))
            article.title = form.cleaned_data ['title']
            article.text = form.cleaned_data ['text']
            article.save()
            return redirect('article:list')
    else:
        form = CreateArticle()
    return render(request, 'articleusers/article_update.html', {'form': form})

@login_required(login_url='/users/login')
def delete_article(request,articleid):
    article = get_object_or_404(Article.objects.all(), author=request.user, pk=int(articleid))
    article.delete()
    return redirect('article:list')


@login_required(login_url='/users/login')
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:list')
    else:
        form = CreateArticle()
    return render(request, 'articleusers/article_create.html', {'form': form})


def signup_view(request):
    if request.POST:
        indexer = True
        form = UserCreationForm(request.POST)
        if form.is_valid():
            x = User()
            x.username = form.cleaned_data ['username']
            x.password = form.cleaned_data ['password1']
            x.save()
            user = form.save()
            login(request, user)
            return redirect('article:list')
    else:
        form = UserCreationForm()
    return render(request, 'articleusers/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('article:list')
    else:
        form = AuthenticationForm()
    return render(request, 'articleusers/login.html', {'form': form})


def get_user_detail(request, userid):
    return render(request, 'articleusers/user_detail.html',
                  {'user': User.objects.all() [int(userid) - 1], 'articles': Article.objects.all()})


def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/users/login/')
