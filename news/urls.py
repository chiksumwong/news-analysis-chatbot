from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters

from news.views import NewsViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'news', NewsViewSet)
 
urlpatterns = [

]
 
urlpatterns += merouter.urls