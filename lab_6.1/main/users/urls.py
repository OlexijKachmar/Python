from . import views
from django.conf.urls import  url

app_name = 'users'
urlpatterns = [
    url(r'signup/$', views.signup_view,name = 'signup'),
    url(r'login/$', views.login_view,name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'^(?P<userid>\d+)/$', views.get_user_detail),
    url(r'^delete-user/(?P<userid>\d+)/$', views.delete_user),
    url(r'articles/$', views.get_article_list, name='articles'),
    url(r'articles/create', views.create_article, name='create'),
    url(r'articles/delete-article/(?P<articleid>\d+)/$', views.delete_article, name='deletear'),
    url(r'articles/change-article/(?P<articleid>\d+)/$',views.put_article,name='changeart')
]