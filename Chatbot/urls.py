from django.conf.urls import url, include
from rest_framework import routers

from news import views_old, views

# Views
router = routers.DefaultRouter()
router.register(r'news', views_old.NewsViewSet)

urlpatterns = [
    url(r'^news/webhook/$', views.elapp),
    url(r'^$', views_old.home),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]