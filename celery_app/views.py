from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_email

# Create your views here.
def index(request):
    send_email.delay()
    return HttpResponse("Hello")