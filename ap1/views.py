from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def Current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s</h1></body></html>"%now
    return HttpResponse(html)

def four_hours_ahead(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours = 4)
    html = "<html><body><h1> After 4 hours, it will be %s </h1></body</html>"%(dt)
    return HttpResponse(html)

def four_hours_before(request):
    dt1 = datetime.datetime.now() + datetime.timedelta(hours = -4)
    html = "<html><body><h1> Before 4 hours, it was %s </h1></body</html>"%(dt1)
    return HttpResponse(html)

def display_string(request, s):
    return HttpResponse(s)
