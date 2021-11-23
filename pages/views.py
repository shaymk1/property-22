from django.http.response import HttpResponse
from django.shortcuts import render,redirect

def home(request):
  context={}
  return render(request, 'pages/home.html', context)


def about(request):
  context = {}
  return render(request, 'pages/about.html', context)
