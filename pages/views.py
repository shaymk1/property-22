from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def home(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices

    }
    return render(request, 'pages/home.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    best_sellers = Realtor.objects.all().filter(is_seller_of_the_month=True)
    context = {
        'realtors': realtors,
        'best_sellers': best_sellers
    }
    return render(request, 'pages/about.html', context)
