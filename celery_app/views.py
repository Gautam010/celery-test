from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sleepy

# Create your views here.
def index(request):
    sleepy()
    return HttpResponse("Hello")