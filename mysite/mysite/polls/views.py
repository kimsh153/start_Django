from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellom world. Your")
# Create your views here.
