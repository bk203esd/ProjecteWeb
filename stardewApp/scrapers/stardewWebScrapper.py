from ..models import Season, Location, Item, Villager, Schedule
from ..scrapers import webScraper_location, webScraper_item, webScraper_villager, webScraper_schedule


# function to begin scraping process
def start():
    print("Starting scraping process...")
