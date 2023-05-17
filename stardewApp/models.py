from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


# Create your models here.
class Season(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=20)
    area = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Villager(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    loved_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='loved_item')
    # loved_item = models.ManyToManyField(Item, related_name='loved_item')
    liked_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='liked_item')
    # liked_item = models.ManyToManyField(Item, related_name='liked_item')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    day_of_week = models.CharField(max_length=20)
    hour = models.CharField(max_length=20)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    villager = models.ForeignKey(Villager, on_delete=models.CASCADE, related_name='villager')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.day_of_week


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'season')


class VillagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'loved_item', 'liked_item')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'hour', 'season', 'villager', 'location')


# Create the root user.
# User.objects.create_superuser('root', 'root@root.com', 'root')
