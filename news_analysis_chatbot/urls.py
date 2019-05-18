from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from news import views
import chatbot
import news
import account

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('chatbot/', include('chatbot.urls')),
    path('api/', include('news.urls')),
    path('api/', include(router.urls)),
    
    path('users/', include('account.urls')),
]
