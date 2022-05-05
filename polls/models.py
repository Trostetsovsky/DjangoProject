from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    place_image = models.ImageField(upload_to='place_photos/%Y/%m/%d/', blank=True)
    likes = models.ManyToManyField(User, related_name='my_likes', blank=True, null=True)
    location = models.ForeignKey('location', on_delete=models.PROTECT, null=True)
    category = models.ForeignKey('category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.ForeignKey('city', on_delete=models.PROTECT, null=True)
    address = models.CharField(max_length=255)
    subway_station = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.city.name + ', ' + self.address


class City(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name

