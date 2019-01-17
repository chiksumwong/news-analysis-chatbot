from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
from rest_framework_mongoengine import viewsets as meviewsets
from news.serializers import NewsSerializer
from news.models import News

import os
import pickle
import json

class NewsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class FakeNewsDector:
    
    """
    Post, get input news then output the result of news
    """
    @csrf_exempt
    def check_news(request):
        # get the input news
        body = json.loads(request.body.decode('utf-8'))
        inputNews = body['text']

        # find the news whether is fake   
        load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'fake_news_detection_model/final_model.sav'), 'rb'))
        prediction = load_model.predict([inputNews])
        probability = load_model.predict_proba([inputNews])
        output = "The news is " + str(prediction[0]) + ", The fake news probability is " + str(probability[0][0]) +"."

        # output the result
        return HttpResponse(output, status=200)