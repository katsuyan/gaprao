"""gaprao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from jugyo import views as jugyo_views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/*', accounts_views.login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/loged_out.html'}),
    url(r'^create_user/$', accounts_views.create_user, name='create_user'),
    url(r'^$', jugyo_views.my_page, name='mypage'),
    url(r'^jugyo/add_mypage/$', jugyo_views.add_mypage, name='add_mypage'),
    url(r'^jugyo/delete_myjugyo/$', jugyo_views.delete_myjugyo, name='delete_myjugyo'),
    url(r'^jugyo/index/$', jugyo_views.index, name='index'),
    url(r'^jugyo/entory/$', jugyo_views.entory, name='entory'),
    url(r'^jugyo/create/$', jugyo_views.create, name='create'),
    url(r'^jugyo/update/(?P<jugyo_id>\d+)/$', jugyo_views.update, name='update'),
    url(r'^jugyo/edit/(?P<jugyo_id>\d+)/$', jugyo_views.edit, name='edit'),
    url(r'^jugyo/delete/(?P<jugyo_id>\d+)/$', jugyo_views.delete, name='delete'),
    url(r'^jugyo/detail/(?P<jugyo_id>\d+)/$', jugyo_views.detail, name='detail')
]
