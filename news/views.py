from django.shortcuts import render

# Create your views here.
from rest_framework_mongoengine import viewsets as meviewsets
from news.serializers import NewsSerializer
from news.models import News
 
class NewsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = News.objects.all()
    serializer_class = NewsSerializer