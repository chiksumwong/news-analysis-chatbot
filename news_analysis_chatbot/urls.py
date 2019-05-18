from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from news import views as NewsViews
from chatbot import views as ChatbotViews

import chatbot
import news
import account

router = DefaultRouter()
router.register(r'news', NewsViews.NewsViewSet)
router.register(r'record', ChatbotViews.RecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('chatbot/', include('chatbot.urls')),
    path('api/', include('news.urls')),
    
    path('user/', include('account.urls')),
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
