from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Mysteria's house, please ring the door bell and wait patiently.")