from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def santhosh(request):
    return HttpResponse('<h1>Sr python developer</h1>')


def pranay(request):
    return HttpResponse('<h1>jr python developer & supporter for santhosh</h1>')