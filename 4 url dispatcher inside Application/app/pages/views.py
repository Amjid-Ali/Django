from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
# Create your views here.


def learn_django(request):
    return HttpResponse("this is msg from pages")
