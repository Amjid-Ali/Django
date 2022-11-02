# Create your views here.
from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
# Create your views here.


def learn_django(request):
    return HttpResponse("this is msg from pages 2")
    # return HttpResponse("this is response from django")

