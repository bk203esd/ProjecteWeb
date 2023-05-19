from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .forms import *
from .models import Season, Location, Item, Villager, Schedule
from .scrapers import stardewWebScrapper


# Create your views here.
@login_required
def create_season(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SeasonForm()
    return render(request, '../templates/web/forms/create_season.html', {'form': form})


class seasonListView(ListView):
    model = Season
    template_name = 'web/lists/season_list.html'
    context_object_name = 'seasons'


def season_detail(request, pk):
    if request.method == 'GET':
        season = get_object_or_404(Season, pk=pk)
        return render(request, '../templates/web/detail/season_detail.html', {'season': season})
    if request.method == 'POST':
        season = get_object_or_404(Season, pk=pk)
        form = SeasonForm(request.POST, instance=season)
        if form.is_valid():
            form.save()
            return redirect('season_list')


def delete_season(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'GET':
        season = get_object_or_404(Season, pk=pk)
        season.delete()
        return redirect('season_list')


@login_required
def create_location(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LocationForm()
    return render(request, '../templates/web/forms/create_location.html', {'form': form})


class locationListView(ListView):
    model = Location
    template_name = 'web/lists/location_list.html'
    context_object_name = 'locations'


def location_detail(request, pk):
    if request.method == 'GET':
        location = get_object_or_404(Location, pk=pk)
        return render(request, '../templates/web/detail/location_detail.html', {'location': location})
    if request.method == 'POST':
        location = get_object_or_404(Location, pk=pk)
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_list')


def delete_location(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'GET':
        location = get_object_or_404(Location, pk=pk)
        location.delete()
        return redirect('location_list')


@login_required
def create_item(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, '../templates/web/forms/create_item.html', {'form': form,
                                                                       'locations': Location.objects.all(),
                                                                       'seasons': Season.objects.all(),
                                                                       })


class itemListView(ListView):
    model = Item
    template_name = 'web/lists/item_list.html'
    context_object_name = 'items'


def item_detail(request, pk):
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=pk)
        return render(request, '../templates/web/detail/item_detail.html',
                      {'item': item, 'locations': Location.objects.all(), 'seasons': Season.objects.all()})
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')


def delete_item(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('item_list')


@login_required
def create_villager(request):
    if request.method == 'POST':
        form = VillagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VillagerForm()
    return render(request, '../templates/web/forms/create_villager.html', {'form': form,
                                                                           'items': Item.objects.all()
                                                                           })


class villagerListView(ListView):
    model = Villager
    template_name = 'web/lists/villager_list.html'
    context_object_name = 'villagers'


def villager_detail(request, pk):
    if request.method == 'GET':
        villager = get_object_or_404(Villager, pk=pk)
        return render(request, '../templates/web/detail/villager_detail.html',
                      {'villager': villager, 'items': Item.objects.all()})
    if request.method == 'POST':
        villager = get_object_or_404(Villager, pk=pk)
        form = VillagerForm(request.POST, instance=villager)
        if form.is_valid():
            form.save()
            return redirect('villager_list')


def delete_villager(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'GET':
        villager = get_object_or_404(Villager, pk=pk)
        villager.delete()
        return redirect('villager_list')


@login_required
def create_schedule(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request, '../templates/web/forms/create_schedule.html', {'form': form,
                                                                           'seasons': Season.objects.all(),
                                                                           'villagers': Villager.objects.all(),
                                                                           'locations': Location.objects.all()
                                                                           })


class scheduleLisTView(ListView):
    model = Schedule
    template_name = 'web/lists/schedule_list.html'
    context_object_name = 'schedules'


def schedule_detail(request, pk):
    if request.method == 'GET':
        schedule = get_object_or_404(Schedule, pk=pk)
        return render(request, '../templates/web/detail/schedule_detail.html',
                      {'schedule': schedule, 'seasons': Season.objects.all(), 'villagers': Villager.objects.all(),
                       'locations': Location.objects.all()})
    if request.method == 'POST':
        schedule = get_object_or_404(Schedule, pk=pk)
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')


def delete_schedule(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'GET':
        schedule = get_object_or_404(Schedule, pk=pk)
        schedule.delete()
        return redirect('schedule_list')


def home(request):
    return render(request, '../templates/web/home.html')


def signup_review(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@api_view(['GET'])
@permission_classes([AllowAny])
def integrateDB(request):
    finalresponse = {}
    stardewWebScrapper.start()
    finalresponse['status'] = 'success'
    return Response(finalresponse, status=status.HTTP_200_OK)
