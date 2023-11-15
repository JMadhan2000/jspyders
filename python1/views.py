from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def harshad(request):
    return HttpResponse('<h1>Sr python developer & one and only django developer in jspiders</h1>')


def rakesh(request):
    return HttpResponse('<h1>jr python developer & supporter for harshad</h1>')