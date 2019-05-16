from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

import chatbot
import news

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^chatbot/', include('chatbot.urls')),
    url(r'^api/', include('news.urls')),
]
