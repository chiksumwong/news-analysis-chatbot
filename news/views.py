from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from news.serializers import NewsSerializer
from news.models import News

from newsplease import NewsPlease

import os
import pickle
import json

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action in ('list',):
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]





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
        load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'model_training/model.sav'), 'rb'))
        prediction = load_model.predict([inputNews])
        probability = load_model.predict_proba([inputNews])
        output = "The news is " + str(prediction[0]) + ", The fake news probability is " + str(probability[0][0]) +"."

        # output the result
        return HttpResponse(output, status=200)

    """
    Post, get input news then output the result of news
    """
    @csrf_exempt
    def check_news_by_url(request):
        # get the input news
        body = json.loads(request.body.decode('utf-8'))
        inputUrl = body['url']

        # get the news text from given url
        article = NewsPlease.from_url(inputUrl)
        inputNews = article.text

        # find the news whether is fake   
        load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'model_training/model.sav'), 'rb'))
        prediction = load_model.predict([inputNews])
        probability = load_model.predict_proba([inputNews])
        output = "The news is " + str(prediction[0]) + ", The fake news probability is " + str(probability[0][0]) +"."

        # output the result
        return HttpResponse(output, status=200)



class NewsInfo:
    """
    Post, get the all news information by given url
    {
        "authors": [],
        "date_download": null,
        "date_modify": null,
        "date_publish": "2017-07-17 17:03:00",
        "description": "Russia has called on Ukraine to stick to the Minsk peace process and disproved claims that Russia is deploying additional troops on the border. Kiev has again accused Russia of invading Ukraine, but has not produced any proof.",
        "filename": "https%3A%2F%2Fwww.rt.com%2Fnews%2F203203-ukraine-russia-troops-border%2F.json",
        "image_url": "https://img.rt.com/files/news/31/9c/30/00/canada-russia-troops-buildup-.si.jpg",
        "language": "en",
        "localpath": null,
        "source_domain": "www.rt.com",
        "text": "Russia has called on Ukraine to stick to the Minsk peace process and disproved claims that Russia is deploying additional troops on the border. Kiev has again accused Russia of invading Ukraine, but has not produced any proof.\nThe calls from Russia come as tension is rising in eastern Ukraine, and rebels say Kiev is preparing to break the ceasefire and resume hostilities.\nAmid the threat of escalation, Russia is calling for a new round of talks in the Belarusian capital, Minsk.\n\u201cWe call for the Minsk process to continue and for a new gathering of the contact group,\u201d Russian presidential adviser Yury Ushakov said Friday.\nNegotiations in Minsk managed to produce a shaky ceasefire in early September, which has mostly held until now. They didn\u2019t stop the violence altogether, as some flare-ups occurred on the border between areas controlled by Kiev loyalists and rebel forces, such as the fighting over the ruins of Donetsk international airport. But the violence was reduced.\nThe calls come after Ukrainian Prime Minister Arseniy Yatsenyuk called this week to abandon the Minsk talks altogether and go back to the Geneva negotiations format from April. Unlike the Kiev talks, the talks in Geneva did not include representatives of the rebel forces.\n\u201cSitting [down] with them for bilateral negotiations is useless,\u201d Yatsenyuk said. \u201cOne of the most efficient and real formats is the Geneva format, which included the participation of the US, the EU, Ukraine and our geographically northern neighbor.\u201d\nThe \u201cnorthern neighbor,\u201d as the Ukrainian PM referred to Russia, argued that the agreement that the Geneva format produced in April failed to stop the violence, because Ukraine never even started to implement the accord and instead of the political reform the agreement called for, sent its troops to shell rebel cities.\nThe exchange comes as amid expectations of a possible resumption of hostilities in Eastern Ukraine. Rebels reported a large build-up of Ukrainian troops near the separation line and said they expected a massive attack at any time. Kiev said the allegations were lies.\nThe rebels have good reasons to suspect foul play from Kiev, considering that a number of high-ranking Ukrainian officials have stated that use of force in the east was needed. The latest statement came Thursday from Markiyan Lubkivskiy, an aide to the head of Ukraine\u2019s Security Service.\n\u201cI believe that sooner or later we will have to start very active actions,\u201d he said on Shuster Live, Ukraine\u2019s main TV talk show on politics.\nEarlier, Yury Lutsenko, an aide to Ukrainian President Petro Poroshenko, said Kiev\u2019s interest in the ceasefire was to win time to regroup its troops.\n\u201cWe need to maintain the ceasefire as long as we can to get our precise instruments, to get military and financial aid from the West,\u201d he said last month. \u201cWe are the ones benefiting from the ceasefire and peace.\u201d\nAccusations of an escalation of tensions have also come this week from Kiev. On Friday a spokesman for the anti-rebel campaign, Andrey Lysenko, claimed that Russia has sent 32 tanks, 16 howitzers, 30 trucks of ammunition and three trucks with radar equipment to rebel-held areas. He offered no evidence of his claim, however.\nKiev has also accused Russia of deploying additional troops along its border with Ukraine this week. The reports even prompted Canadian Foreign Minister John Baird to condemn Russia on Wednesday.\n\u201cWe strongly condemn these provocative actions by Russia, and we believe this is further proof that the Kremlin only seeks to hamper the peace process in Ukraine,\u201d Baird said in a statement.\nThis provoked a sarcastic response from the Russia Defense Ministry, which said the reports were not true and that Canada should address its concerns to those producing the rumors, rather than to Russia.\n\u201cAll such provocative \u2018reports\u2019 aimed at further escalating the tension over the civil conflict in southeast Ukraine have a single source. The source is not Ukrainian, although it currently operates from one of the governmental buildings in Kiev,\u201d the statement said, apparently alleging to the heavy presence of American personnel in the Ukrainian Security Service.\nTensions in Eastern Ukraine are also on the rise after the self-proclaimed Donetsk and Lugansk People\u2019s Republics held elections last week.\nUkraine and its sponsors branded the ballot an irrelevant mockery and a violation of the Minsk agreement. Russia said it respected the choice of the people living in the breakaway regions, but stopped short of formally recognizing them, a move that Washington said would lead to further economic sanctions against Russia.",
        "title": "Moscow to Kiev: Stick to Minsk ceasefire, stop making false \u2018invasion\u2019 claims",
        "title_page": null,
        "title_rss": null,
        "url": "https://www.rt.com/news/203203-ukraine-russia-troops-border/"
    }
    """


    """
    Post, get the all news information by given url
    """
    @csrf_exempt
    def get_news_info_from_url(request):
        # get the input news url
        body = json.loads(request.body.decode('utf-8'))
        inputNews = body['url']

        # find the news textual
        article = NewsPlease.from_url(inputNews)
        authors = article.authors # list format
        date_publish = article.date_publish # date time format
        
        # following are string
        source_domain = article.source_domain
        url = article.url
        title = article.title
        text = article.text

        # toJson
        # output = Object()
        # output.authors = authors
        # output.date_publish = date_publish
        # output.source_domain = source_domain
        # output.url = url
        # output.title = title
        # output.text = text

        # output the result
        # return HttpResponse(output.toJSON(), status=200)
        return HttpResponse("The news Info are: " + title, status=200)

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)