from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'signIn.html')


def moosa(request):
    print(request.GET.get('email', 'No email provided'))
    print(request.GET.get('password', 'No password provided'))
    return HttpResponse("You have submitted credentials")
