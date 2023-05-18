from stardewApp.scrapers.webScraper_schedule import ScrapSchedule
from stardewApp.models import *


def do_Schedule():
    villager = Villager()
    villager.name = 'Alex'

    scrap_schedule = ScrapSchedule()
    schedule = scrap_schedule.get_data(villager)
    print(schedule)
