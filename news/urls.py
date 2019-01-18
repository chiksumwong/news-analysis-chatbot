from django.urls import path
from rest_framework_mongoengine import routers as merouters

from news.views import NewsViewSet
from news.views import FakeNewsDector

merouter = merouters.DefaultRouter()
merouter.register(r'news', NewsViewSet)
 
urlpatterns = [
    path('checknews/', FakeNewsDector.check_news),
    path('checknewsbyurl/', FakeNewsDector.check_news_by_url),
    path('info/', FakeNewsDector.get_news_info),
]
 
urlpatterns += merouter.urls