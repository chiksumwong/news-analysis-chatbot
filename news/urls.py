from django.urls import path

from news import views
 
urlpatterns = [
    path('checknews/', views.FakeNewsDector.check_news),
    path('checknewsbyurl/', views.FakeNewsDector.check_news_by_url),

    path('newsinfo/', views.NewsInfo.get_news_info_from_url),
]
 