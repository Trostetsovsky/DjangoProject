from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from polls.views import index, detail, profile, city, search, login, register

urlpatterns = [
    path('', index, name='index'),
    # path('', IndexHome.as_view(), name='index'),
    path('place/<slug:place_slug>/', detail, name='detail'),
    path('profile/<str:username>/', profile, name='profile'),
    path('city/<slug:city_name>/', city, name='city'),
    # path('city/<slug:city_name>/', CityIndexHome.as_view(), name='city'),
    path('search/', search, name='search'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)