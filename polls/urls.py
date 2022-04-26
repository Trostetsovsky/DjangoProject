from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from polls.views import index, detail, profile, city

urlpatterns = [
    path('', index, name='index'),
    path('place/<slug:place_slug>/', detail, name='detail'),
    path('profile/<str:username>/', profile, name='profile'),
    path('city/<slug:city_name>/', city, name='city')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)