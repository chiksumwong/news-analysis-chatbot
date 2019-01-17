from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters

from chatbot.views_web import NewsViewSet
from chatbot import views

merouter = merouters.DefaultRouter()
merouter.register(r'web', NewsViewSet)

urlpatterns = [
    url('^webhook/', views.webhook),
]

urlpatterns += merouter.urls