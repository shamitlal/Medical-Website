from django.conf.urls import include, url
from . import views


urlpatterns = [
    

    url(r'^$',views.video_chat,name='video_chat'),

    
]