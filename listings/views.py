from django.shortcuts import render


def home(request):
  context = {}
  return render(request, 'listings/listings.html', context)

def listing(request):
  context = {}
  return render(request, 'listings/listing.html', context)

def search(request):
  context = {}
  return render(request, 'listings/search.html', context)
