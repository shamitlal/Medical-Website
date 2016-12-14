from django.conf.urls import include, url
from . import views

app_name = 'login'

urlpatterns = [
    #/music/
    
    #comment for video 29:generic views
    #url(r'^$',views.index,name='index'),

    #/music/712/
    #url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),

    #/music/712/favourite
    #url(r'^(?P<album_id>[0-9]+)/favourite$',views.favourite, name='favourite'),
    
   

    url(r'^$',views.register_login,name='register_login'),
    url(r'^logout/$',views.logout_page,name='logout_page'),

    
]