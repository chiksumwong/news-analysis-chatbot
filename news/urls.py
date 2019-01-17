from django.urls import path
from rest_framework_mongoengine import routers as merouters

from news.views import NewsViewSet
from news.views import FakeNewsDector

merouter = merouters.DefaultRouter()
merouter.register(r'news', NewsViewSet)
 
urlpatterns = [
    path('checknews/', FakeNewsDector.check_news)
]
 
urlpatterns += merouter.urls