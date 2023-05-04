from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SeasonForm, LocationForm, ItemForm, VillagerForm, ScheduleForm


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
    return render(request, '../templates/forms/create_season.html', {'form': form})


@login_required
def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LocationForm()
    return render(request, '../templates/forms/create_location.html', {'form': form})


@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, '../templates/forms/create_item.html', {'form': form})


@login_required
def create_villager(request):
    if request.method == 'POST':
        form = VillagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VillagerForm()
    return render(request, '../templates/forms/create_villager.html', {'form': form})


@login_required
def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request, '../templates/forms/create_schedule.html', {'form': form})


def home(request):
    return render(request, '../templates/home.html')
