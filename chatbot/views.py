from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        

        # Identify the request whether come from Line Server
        signature = request.META.get("HTTP_X_LINE_SIGNATURE")

        # Get the request body from Line Server
        body = request.body.decode('utf-8')

        try:
            # Parse all event with them row
            events = parser.parse(body, signature)
        except InvalidSignatureError:                      # If the request is not come form Line Server
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()


        for event in events:
            if isinstance(event, MessageEvent):            # Make sure the even is 'Message Event'
                if isinstance(event.message, TextMessage): # Make sure the message is 'Text Message'
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )

                
        return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest()