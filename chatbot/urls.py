from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters

from chatbot import views_web
from chatbot import views

merouter = merouters.DefaultRouter()
merouter.register(r'web', views_web.NewsViewSet)

urlpatterns = [
    url('^webhook/', views.webhook),
]

urlpatterns += merouter.urls