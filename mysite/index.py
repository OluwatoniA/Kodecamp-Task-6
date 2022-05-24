from django.http import HttpResponse
from django.shortcuts import render


def webpage1(request):
    return render(request, 'page 1.html')

def webpage2(request):
    return render(request, 'page 2.html')

def webpage3(request):
    return render(request, 'page 3.html')     