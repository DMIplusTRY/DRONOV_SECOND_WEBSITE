from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("200 Ok")

def promo(response):
    return HttpResponse("2000 Ok")