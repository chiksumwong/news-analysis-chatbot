from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from news_analysis_chatbot import views
import chatbot
import news


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^chatbot/', include('chatbot.urls')),
    url(r'^api/', include('news.urls')),
]