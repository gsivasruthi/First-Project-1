from django.shortcuts import render








from django.http import HttpResponse

# Create your views here.
def propose(request):
    return HttpResponse('<marquee>Yes I Love U Too</marquee>')

