from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string_response(request):
    return HttpResponse("this is my frst response")
def second_response(request):
    return HttpResponse("this is second resoponse")