from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'main'

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.homepage,name = "homepage"),
    url(r'users/', include('users.urls')),
]