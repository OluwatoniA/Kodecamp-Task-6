from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def about(request):
    return HttpResponse('about')

def contact(request):
    return HttpResponse('contact')      


# Create your views here.
