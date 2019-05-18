import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

from newsplease import NewsPlease

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from chatbot.serializers import RecordSerializer

from chatbot.models import Record as ChatbotModels
from news.models import News as NewsModels

import pickle


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def webhook(request):
    if request.method == 'POST':

        # Identify the request whether come from Line Server
        signature = request.META.get("HTTP_X_LINE_SIGNATURE")
        # Get the request body from Line Server
        body = request.body.decode('utf-8')


        # Parse all event with them row
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:              # If the request is not come form Line Server
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()


        # Handle each event
        for event in events:
            # Make sure the even is 'Message Event'
            if isinstance(event, MessageEvent):
                print('event form line: ', event)

                # Make sure the message is 'Text Message'
                if isinstance(event.message, TextMessage):
                    if event.message.text.startswith('Real News'):
                        help_label("True", event.reply_token, event.source.user_id)
                    elif event.message.text.startswith('Fake News'):
                        help_label("False", event.reply_token, event.source.user_id)
                    elif event.message.text.startswith('http'):
                        # detect the fake news by url
                        print(event.message.text)
                        reply_text = detect_fake_news_by_url(event.source.user_id, event.message.text)
                        # Reply to Line
                        reply_to_line(event.reply_token, event.source.user_id, reply_text)
                    else:
                        # detect the fake news
                        print(event.message.text)
                        reply_text = detect_fake_news(event.source.user_id, event.message.text)
                        # Reply to Line
                        reply_to_line(event.reply_token, event.source.user_id, reply_text)

        # Response 200
        return HttpResponse(reply_text, status=200)
    else:
        return HttpResponseBadRequest()




# Reply to Line
def reply_to_line(reply_token, user_id, reply_text):
    if reply_text == None:
        return None

    button_template_message = ButtonsTemplate(
        title = "News Analysis Result",
        text = reply_text,
        actions=[
            MessageTemplateAction(
                label='Real News', text='Real News'
            ),
            MessageTemplateAction(
                label='Fake News', text='Fake News'
            )
        ]
    )
    
    try:
        line_bot_api.push_message(user_id, TemplateSendMessage(alt_text="Please Use in Phone", template=button_template_message))
    except LineBotApiError as e:
        # error handle
        raise e



# handle the helper
def help_label(input_label, reply_token, userId):

    # get statement by channel id (user id)
    data = ChatbotModels.objects.raw('SELECT * FROM record WHERE channel = %s ORDER BY ID DESC LIMIT 1', [userId])
    print(data.statement)

    # update statement
    updateData=NewsModels.objects.filter(statement=data.statement)
    updateData.update(label = input_label)

    reply_text = "Thank you for helping to improve the accuracy of the classifier!"

    # Reply to Line
    line_bot_api.reply_message(reply_token, TextSendMessage(text=reply_text))
    


# Detect the fake news
def detect_fake_news(userId, text):
    load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'model_training/model.sav'), 'rb'))
    prediction = load_model.predict([text])
    probability = load_model.predict_proba([text])

    # inset to database
    ChatbotModels.objects.create(channel=userId, text=text, result=prediction, probability=probability)

    # inset to news
    NewsModels.objects.create(statement=text, label="NONE")

    output = "News is " + str(prediction[0]) + ",Fake news probability is " + str('%.2f' % probability[0][0]+".You think it is")
    return output

# Detect the fake news
def detect_fake_news_by_url(userId, inputUrl):
    # get the news text from given url
    article = NewsPlease.from_url(inputUrl)
    inputNews = article.text
    print("Input Text: " + inputNews)
    # find the news whether is fake   
    load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'model_training/model.sav'), 'rb'))
    prediction = load_model.predict([inputNews])
    probability = load_model.predict_proba([inputNews])

    # inset to database
    ChatbotModels.objects.create(channel=userId, text=inputNews, result=prediction, probability=probability)

    # inset to news
    NewsModels.objects.create(statement=inputNews, label="NONE")

    output = "News is " + str(prediction[0]) + ",Fake news probability is " + str('%.2f' % probability[0][0]+".You think it is")
    return output


class RecordViewSet(viewsets.ModelViewSet):
    queryset = ChatbotModels.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action in ('list',):
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]