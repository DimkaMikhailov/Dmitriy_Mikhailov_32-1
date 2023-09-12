from django.shortcuts import HttpResponse
from datetime import datetime


def helo(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project", 200)


def date_now(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now().strftime('%Y-%m-%d'), 200)


def buy(request):
    if request.method == 'GET':
        return HttpResponse("Good buy user!", 200)

