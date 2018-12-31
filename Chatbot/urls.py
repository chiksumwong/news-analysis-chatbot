from django.conf.urls import url, include
from rest_framework import routers

from news import views

# Views
router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]