from django.shortcuts import render
 
from rest_framework_mongoengine import viewsets as meviewsets
from chatbot.serializers import NewsSerializer
from chatbot.models import News
 
class NewsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = News.objects.all()
    serializer_class = NewsSerializer