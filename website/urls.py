"""website URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^disease/', include('disease.urls')),
    url(r'^general/', include('general.urls')),
    url(r'^register/', include('login.urls')),
    url(r'^medworld/', include('cover.urls')),
    url(r'^about_us/', include('about_us.urls')),
    url(r'^video_chat/', include('video_chat.urls')),
    url(r'^homeopathy/', include('homeopathy.urls')),
    url(r'^ayurveda/', include('ayurveda.urls')),
    url(r'^allopathy/', include('allopathy.urls')),
    url(r'^healthcare_media/', include('healthcare_media.urls')),
    

]
