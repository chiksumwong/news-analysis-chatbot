from django.conf.urls import url

from . import views

urlpatterns = [
    url('^webhook/', views.webhook),
]