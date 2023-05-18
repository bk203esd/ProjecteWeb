"""projecteWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from oauth2_provider.views import TokenView
from stardewApp.views import create_season, create_location, create_item, create_villager, create_schedule, home, \
    seasonListView, locationListView, itemListView, villagerListView, scheduleLisTView, season_detail, location_detail, \
    item_detail, villager_detail, schedule_detail, signup_review

urlpatterns = [
    path('', home, name='home'),

    # admin site
    path('admin/', admin.site.urls),

    # forms site
    path('seasons/add/', create_season, name='seasons_add'),
    path('locations/add/', create_location, name='locations_add'),
    path('items/add/', create_item, name='items_add'),
    path('villagers/add/', create_villager, name='villagers_add'),
    path('schedules/add/', create_schedule, name='schedules_add'),

    # list site
    path('seasons/', seasonListView.as_view(), name='season_list'),
    path('locations/', locationListView.as_view(), name='location_list'),
    path('items/', itemListView.as_view(), name='item_list'),
    path('villagers/', villagerListView.as_view(), name='villager_list'),
    path('schedules/', scheduleLisTView.as_view(), name='schedule_list'),

    # detail site
    path('seasons/<int:pk>/', season_detail, name='season_detail'),
    path('locations/<int:pk>/', location_detail, name='location_detail'),
    path('items/<int:pk>/', item_detail, name='item_detail'),
    path('villagers/<int:pk>/', villager_detail, name='villager_detail'),
    path('schedules/<int:pk>/', schedule_detail, name='schedule_detail'),

    # account site
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/signup/', signup_review, name='signup'),

    # login site
    path('api/token/', TokenView.as_view(), name='token'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]
