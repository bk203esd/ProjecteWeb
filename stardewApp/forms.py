from django import forms
from .models import Season, Location, Item, Villager, Schedule


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = '__all__'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class VillagerForm(forms.ModelForm):
    class Meta:
        model = Villager
        fields = '__all__'


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'



