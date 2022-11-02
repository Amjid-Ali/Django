from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
# Create your views here.


def learn_django(request):
    data = 10
    return HttpResponse(data)
    # return HttpResponse("this is response from django")


def ld(request):
    return HttpResponse("<h1>this is response from django</h1>")
