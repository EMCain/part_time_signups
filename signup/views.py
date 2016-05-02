from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hello, welcome to the part time sign up app.")