from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

import chatbot

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', chatbot.views_home.home),
    url(r'^chatbot/', include('chatbot.urls')),
]
