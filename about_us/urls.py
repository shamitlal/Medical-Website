from django.conf.urls import include, url
from . import views


urlpatterns = [
    

    url(r'^$',views.about_us,name='about_us'),

    
]