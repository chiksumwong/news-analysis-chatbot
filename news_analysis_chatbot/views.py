from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def home (request):
    return HttpResponse("Welcome", status=200)