from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>")