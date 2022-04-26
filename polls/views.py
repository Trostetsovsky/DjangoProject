from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from polls.models import Place, Category, Location

city_list = [
    {'title': 'Москва', 'url_name': 'moscow'},
    {'title': 'Санкт-Петербург', 'url_name': 'saint-petersburg'},
    {'title': 'Казань', 'url_name': 'kazan'},
    {'title': 'Екатеринбург', 'url_name': 'ekaterinburg'},
]


def index(request):
    place = Place.objects.all()
    context = {
        'places': place,
        'city_list': city_list,
    }
    return render(request, 'polls/index.html', context=context)


def detail(request, place_slug):
    place = get_object_or_404(Place, slug=place_slug)
    context = {
        'places': place,
        'city_list': city_list,
    }
    return render(request, 'polls/place_detail.html', context=context)


def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'polls/profile.html', {'user': user})


def city(request, city_name):
    places = Place.objects.filter(location__slug=city_name)
    context = {
        'places': places,
        'city_list': city_list,
        'city_name': city_name,
    }
    return render(request, 'polls/city_detail.html', context=context)
