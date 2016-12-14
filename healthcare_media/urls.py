from django.conf.urls import include, url
from . import views


urlpatterns = [
    

    url(r'^$',views.healthcare_media,name='healthcare_media'),

    
]