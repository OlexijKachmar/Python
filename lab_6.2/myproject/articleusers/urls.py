from . import  views
from django.conf.urls import url

app_name = 'article'
urlpatterns = [
    url(r'^signup/$', views.signup_view,name = "signup"),
    url(r'login/$', views.login_view,name='login'),
    url(r'^(?P<userid>\d+)/$', views.get_user_detail),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'^article$', views.get_article_list, name="list"),
    url(r'^article/create-article/$', views.article_create, name='create'),
    url(r'article/put/(?P<articleid>\d+)/$', views.put_article, name='put'),
    url(r'article/delete/(?P<articleid>\d+)/$',views.delete_article,name='delete'),
]
