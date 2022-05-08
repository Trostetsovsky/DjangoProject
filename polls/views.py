from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from polls.forms import UserRegistrationForm
from polls.models import Place, Category, Location

city_list = [
    {'title': 'Москва', 'url_name': 'moscow'},
    {'title': 'Санкт-Петербург', 'url_name': 'saint-petersburg'},
    {'title': 'Казань', 'url_name': 'kazan'},
    {'title': 'Екатеринбург', 'url_name': 'ekaterinburg'},
]


def index(request):
    places = Place.objects.all()
    paginator = Paginator(places, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'city_list': city_list,
        'title': 'Главная',
        'page_obj': page_obj,
    }
    return render(request, 'polls/index.html', context=context)


# class IndexHome(ListView):
#     paginate_by = 2
#     model = Place
#     template_name = 'polls/index.html'
#     context_object_name = 'places'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная'
#         context['city_list'] = city_list
#         return context

    # def get_queryset(self):
    #     return Place.objects.all()


def detail(request, place_slug):
    place = Place.objects.select_related('location__city').get(slug=place_slug)
    context = {
        'places': place,
        'city_list': city_list,
        'title': place.name,
    }
    return render(request, 'polls/place_detail.html', context=context)


def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'polls/profile.html', {'user': user})


def city(request, city_name):
    places = Place.objects.filter(location__city__slug=city_name)
    context = {
        'places': places,
        'city_list': city_list,
        'city_name': city_name,
        'title': city_name,
    }
    return render(request, 'polls/city_detail.html', context=context)


# class CityIndexHome(ListView):
#     paginate_by = 2
#     model = Place
#     template_name = 'polls/city_detail.html'
#     context_object_name = 'places'
#
#     def get_queryset(self):
#         return Place.objects.filter(location__city__slug=self.kwargs['city_name'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['city_name'] = self.kwargs['city_name']
#         context['city_list'] = city_list
#         context['title'] = context['city_name']
#         return context


# class SearchResults(ListView):
#     model = Place
#     template_name = 'polls/search.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Place.objects.filter(
#             Q(name__icontains=query) | Q(slug__icontains=query)
#         )
#         print(object_list)
#         return object_list


def search(request):
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        places = Place.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query)
        )
        return render(request, 'polls/search.html', context={'places': places, 'query': query})
    else:
        return redirect('index')


def login(request):
    return HttpResponse('aboba')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'polls/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'polls/register.html', {'user_form': user_form})
