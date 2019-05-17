import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

from newsplease import NewsPlease

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
                        reply_text = "Thank you for helping to improve the accuracy of the classifier!"
                        v_response(event.reply_token, reply_text)
                    elif event.message.text.startswith('Fake News'):
                        reply_text = "Thank you for helping to improve the accuracy of the classifier!"
                        v_response(event.reply_token, reply_text)
                    elif event.message.text.startswith('http'):
                        # detect the fake news by url
                        print(event.message.text)
                        reply_text = detect_fake_news_by_url(event.message.text)
                        # Reply to Line
                        reply_to_line(event.reply_token, event.source.user_id, reply_text)
                    else:
                        # detect the fake news
                        print(event.message.text)
                        reply_text = detect_fake_news(event.message.text)
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

# Reply to Line
def v_response(reply_token, reply_text):
    if reply_text == None:
        return None
    line_bot_api.reply_message(reply_token, TextSendMessage(text=reply_text))

# Detect the fake news
def detect_fake_news(text):
    load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'model_training/model.sav'), 'rb'))
    prediction = load_model.predict([text])
    probability = load_model.predict_proba([text])

    output = "News is " + str(prediction[0]) + ",Fake news probability is " + str('%.2f' % probability[0][0]+".You think it is")
    return output

# Detect the fake news
def detect_fake_news_by_url(inputUrl):
    # get the news text from given url
    article = NewsPlease.from_url(inputUrl)
    inputNews = article.text
    print("Input Text: " + inputNews)
    # find the news whether is fake   
    load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'model_training/model.sav'), 'rb'))
    prediction = load_model.predict([inputNews])
    probability = load_model.predict_proba([inputNews])
    output = "News is " + str(prediction[0]) + ",Fake news probability is " + str('%.2f' % probability[0][0]+".You think it is")
    return output
