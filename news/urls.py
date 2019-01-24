from django.urls import path
from rest_framework_mongoengine import routers as merouters

from news.views import NewsViewSet
from news.views import FakeNewsDector
from news.views import NewsInfo

merouter = merouters.DefaultRouter()
merouter.register(r'news', NewsViewSet)
 
urlpatterns = [
    path('checknews/', FakeNewsDector.check_news),
    path('checknewsbyurl/', FakeNewsDector.check_news_by_url),
    path('info/', FakeNewsDector.get_news_info),
    path('newsinfo/', NewsInfo.get_news_info_from_url),
]
 
urlpatterns += merouter.urls