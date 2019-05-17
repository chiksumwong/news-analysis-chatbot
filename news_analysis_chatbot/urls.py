from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from news import views

import chatbot
import news

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chatbot/', include('chatbot.urls')),
    url(r'^api/', include('news.urls')),
    url(r'^api/', include(router.urls))
]
