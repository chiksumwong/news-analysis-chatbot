from news.models import News
from news.serializers import NewsSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django.http import HttpResponse

def home (request):
    return Response("Welcome", status=status.HTTP_201_CREATED)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    parser_classes = (JSONParser,)

    def get_permissions(self):
        if self.action in ('create',): #Create = Post method
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    # [GET] api/news/
    def list(self, request, **kwargs):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # [POST] api/news/
    @permission_classes((IsAuthenticated,))
    def create(self, request, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)