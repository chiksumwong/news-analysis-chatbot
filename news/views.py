from news.models import News
from news.serializers import NewsSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
# Have all CURD functions, since 'ModelViewSet' define all CURD functions