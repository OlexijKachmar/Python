from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User, Article
from .forms import RegistrationForm, LoginForm, CreateArticle

users_arr = []
users_arr = [User()]
users_arr [0].password = '2906alex'
users_arr [0].username = 'alex'

l = []
for i in range(3):
    l.append(Article())
l [0].author = 'Alex Kurtsman'
l [0].checked = True
l [0].title = 'Real Talk'
l [0].text = 'R'

l [1].author = 'Conor McGregor'
l [1].checked = True
l [1].title = 'My Fight'
l [1].text = 'My Battle'

l [2].author = 'Oleksii Havryshkiv'
l [2].checked = True
l [2].title = 'I have felt'
l [2].text = "Я в своем познании настолько преисполнился, что я как будто бы уже "

logged_user = 0

#@login_required(login_url ='/users/articles/')
def create_article(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST)
        if form.is_valid():
            x = Article()
            x.text = str(form.cleaned_data ['text'])
            x.title = str(form.cleaned_data ['title'])
            x.author = users_arr[logged_user].username
            l.append(x)
            users_arr[logged_user].articles.append(x)
            return redirect('users:articles')
    else:
        form = CreateArticle()
    return render(request, 'users/article_create.html', {'form': form})

number_of_article_to_change = 0

def put_article(request,articleid):
    if len(users_arr[logged_user].articles) == 0:
        return redirect('users:articles')
    global number_of_article_to_change
    if request.method == 'POST':
        form = CreateArticle(request.POST)
        if form.is_valid():
            x = Article()
            x.text = str(form.cleaned_data ['text'])
            x.title = str(form.cleaned_data ['title'])
            x.author = users_arr[logged_user].username
            l[number_of_article_to_change] = x
            users_arr[logged_user].articles[int(articleid) - 1] = x
            return redirect('users:articles')
    else:
        users_arr[logged_user].articles[int(articleid) - 1].checked = False
        for i in range(len(l)):
            if l[i].author == users_arr[logged_user].username and l[i].title == users_arr[logged_user].articles[int(articleid) - 1]:
                number_of_article_to_change = i
        form = CreateArticle()
    return render(request, 'users/article_create.html', {'form': form})

def signup_view(request):
    if request.POST:
        indexer = True
        form = RegistrationForm(request.POST)
        if form.is_valid():
            for i in users_arr:
                if str(i.password) == str(form.cleaned_data ['password']) or str(i.username) == str(
                        form.cleaned_data ['login']):
                    indexer = False
            if indexer:
                global logged_user
                x = User()
                x.username = str(form.cleaned_data ['login'])
                x.password = str(form.cleaned_data ['password'])
                users_arr.append(x)
                logged_user = len(users_arr) - 1
                return redirect('users:articles')
    else:
        form = RegistrationForm()
    return render(request, 'users/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            for i in range(len(users_arr)):
                if str(users_arr [i].username) == str(form.cleaned_data ['login']) and str(
                        users_arr [i].password) == str(form.cleaned_data ['password']):
                    global logged_user
                    logged_user = i
                    return redirect('users:articles')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    return redirect('http://127.0.0.1:8000/users/login')


def get_user_detail(request, userid):
    return render(request, 'users/user_detail.html', {'user': users_arr[int(userid) - 1]})

def delete_user(request, userid):
    users_arr.pop(int(userid) - 1)
    return render(request, 'users/user_detail.html', {'user': users_arr[int(userid) - 2]})

def get_article_list(request):
    return render(request, 'users/articles_list.html', {'articles': l})

def delete_article(request, articleid):
    l.pop(int(articleid) - 1)
    return redirect('users:articles')
