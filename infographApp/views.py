from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'signIn.html')


def info(request):
    return HttpResponse("This is information")
