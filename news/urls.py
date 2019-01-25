from django.urls import path
from rest_framework_mongoengine import routers as merouters

from news import views

merouter = merouters.DefaultRouter()
merouter.register(r'news', views.NewsViewSet)
 
urlpatterns = [
    path('checknews/', views.FakeNewsDector.check_news),
    path('checknewsbyurl/', views.FakeNewsDector.check_news_by_url),
    path('info/', views.FakeNewsDector.get_news_info),
    path('newsinfo/', views.NewsInfo.get_news_info_from_url),
]
 
urlpatterns += merouter.urls