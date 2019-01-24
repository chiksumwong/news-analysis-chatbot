import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

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
                # Make sure the message is 'Text Message'
                if isinstance(event.message, TextMessage):
                    reply_text = detect_fake_news(event.message.text)
                    # Reply to Line
                    reply_to_line(event.reply_token, reply_text)


        # Response 200
        return HttpResponse(reply_text, status=200)
    else:
        return HttpResponseBadRequest()


# Reply to Line
def reply_to_line(reply_token, reply_text):
    if reply_text == None:
        return None

    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=reply_text)
    )


# Detect the fake news
def detect_fake_news(text):
    load_model = pickle.load(open(os.path.join(settings.BASE_DIR, 'fake_news_detection_model/final_model.sav'), 'rb'))
    prediction = load_model.predict([text])
    probability = load_model.predict_proba([text])

    output = "The news is " + str(prediction[0]) + ", The fake news probability is " + str(probability[0][0]) +"."
    return output

# Keywork Reply
# def keywork_reply(received_text):
#     if received_text =='news:':


#     return 'bad'
