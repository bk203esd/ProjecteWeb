from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import *
from .models import Season, Location, Item, Villager, Schedule


# Create your views here.
@login_required
def create_season(request):
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


@login_required
def create_location(request):
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


@login_required
def create_item(request):
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


@login_required
def create_schedule(request):
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


def home(request):
    return render(request, '../templates/web/home.html')
