import os
import random

from ..models import Season, Location, Item, Villager, Schedule
from ..scrapers import webScraper_location, webScraper_item, webScraper_villager, webScraper_schedule, webScraper_season
from django.contrib.auth.models import User


# function to begin scraping process
def start():
    print("Starting scraping process...")
    # create user Scraper and Superusers django
    os.system('python manage.py createsuperuser --noinput')
    user = User.objects.update_or_create(username='Scraper', password='1234')
    # execute scrap season
    seasons = webScraper_season.ScrapSeason()
    seasons.get_data()
    # create season objects
    for season in seasons.data:
        season = season.strip()
        Season.objects.update_or_create(name=season)
    season = Season.objects.update_or_create(name='N/A')
    print("Seasons created")

    # execute scrap location
    locations = webScraper_location.ScrapLocation()
    locations.get_data()
    # create location objects
    for location in locations.data:
        location = location.strip()
        Location.objects.update_or_create(name=location, defaults={'area': 'N/A'})
    location = Location.objects.update_or_create(name='N/A', defaults={'area': 'N/A'})
    print("Locations created")

    # execute scrap item
    # first Forage Items
    items = webScraper_item.ForageScrape()
    items = items.parse_items()
    del items[""]
    # create item objects
    for item in items:
        if len(items[item].locations) == 0:
            items[item].locations = ['N/A']
        auxitem = items[item]
        auxitem.locations = auxitem.locations[0].strip()
        location = Location.objects.get_or_create(name=auxitem.locations, defaults={'area': 'N/A'})
        season = Season.objects.get_or_create(name=auxitem.season.strip())
        Item.objects.update_or_create(name=auxitem.name, location=location[0], season=season[0],
                                      category='Forage')
    print("Forage Items created")

    # second Cooking/Crops Items
    items = webScraper_item.CookingScrape()
    items = items.parse_items()
    del items[""]
    # create item objects
    Location.objects.update_or_create(name='Farm', defaults={'area': 'N/A'})
    for item in items:
        if type(items[item].locations) is not list:
            items[item].locations = ['Farm']
        auxitem = items[item]
        auxitem.locations = auxitem.locations[0].strip()
        location = Location.objects.get_or_create(name=auxitem.locations, defaults={'area': 'N/A'})
        season = Season.objects.get_or_create(name=auxitem.season.strip())
        Item.objects.update_or_create(name=auxitem.name, location=location[0], season=season[0], category='Cooking')
    print("Cooking Items created")

    # third Minerals Items

    # execute scrap villager
    villagers = {}
    villagers_names = webScraper_villager.VillagerScrap().get_names_data()
    for index, villager_name in enumerate(villagers_names):
        if villager_name != 'Krobus':
            villagers[villager_name] = webScraper_villager.Villager(name=villager_name)
        if index > 32: break

    for villager in villagers:
        villager_name = villager
        villager = webScraper_villager.VillagerScrap().get_villager_data(villager)
        if type(villager['love']) is not list:
            villager['love'] = [villager['love']]
        if type(villager['like']) is not list:
            villager['like'] = [villager['like']]
        loved_item = Item.objects.get_or_create(name=villager['love'][0],
                                                defaults={'location': location[0], 'season': season[0],
                                                          'category': 'N/A'})
        liked_item = Item.objects.get_or_create(name=villager['like'][0],
                                                defaults={'location': location[0], 'season': season[0],
                                                          'category': 'N/A'})
        villager = Villager.objects.update_or_create(name=villager_name, birthday=villager['birthday'],
                                                     loved_item=loved_item[0],
                                                     liked_item=liked_item[0], user=user[0])

    print("Villagers created")

    # execute scrap schedule
    hours = ['11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # get villager DB
    villagers = Villager.objects.all()
    # get location DB
    locations = Location.objects.all()
    location_count = Location.objects.count()
    # get season DB
    seasons = Season.objects.all()
    # for each villager in DB
    for villager in villagers:
        # for each season in DB
        for season in seasons:
            # update schedule
            num = random.randint(0, location_count - 1)
            auxvillager = Villager.objects.get_or_create(name=villager)
            auxlocation = Location.objects.get_or_create(name=locations[num])
            auxseason = Season.objects.get_or_create(name=season)
            Schedule.objects.update_or_create(villager=auxvillager[0], location=auxlocation[0], season=auxseason[0],
                                              day_of_week=random.choice(days_of_week), hour=random.choice(hours))

    print("Schedules created")
    # clean location with name "F"
    # Location.objects.filter(name='F').delete()
