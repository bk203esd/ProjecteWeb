import urllib3
import bs4
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projecteWeb.settings')
django.setup()
from stardewApp.models import Villager

# Global variables needed to get the villager's Schedule
dailySchedule = []
fullParsedSchedule = []

""" Used for villagers whose schedule depends on the season """


def parseFullSchedule(name, day):
    # Get actual season name
    name = name.text.split('\xa0')
    if len(name) == 2:
        name = name[1]
    else:
        name = name[0]

    # Start parsing seasons schedule
    for tag in day.find_all('p'):
        # p -> Type of the day (Raining, Monday, ...)
        title = tag.text.split('\n')
        tempDay = title[0]  # Store it for later

        # Schedule for the day
        for schedule in day.find_all('table', attrs={'class': 'wikitable'}):
            dayInfo = schedule.text.split('\n')
            count = 0
            tempPairs = []
            for item in dayInfo:
                # Here we have pairs [Time, Location, T, L, T, L, ...]
                if item != '' and item != 'Time' and item != 'Location':
                    if count % 2 == 0:
                        tempTime = item  # Store until associated location
                        count += 1
                    else:
                        tempPairs.append((tempTime, item))  # Store final pair
                        count += 1
        dailySchedule.append((tempDay, tempPairs))  # Assign day to full schedule
    fullParsedSchedule.append((name, dailySchedule))  # Store final season schedule


""" Used for villagers whose schedule depends only on the day """


def parseWeakSchedule(name, day):
    # Type of the day (Raining, Monday, ...)
    name = name.text.split('\n')[0]
    # Schedule for the day
    count = 0
    for scheduleInfo in day.find_all('td'):
        if count % 2 == 0:
            tempTime = scheduleInfo.text.split('\n')[0]  # Store until associated location
            count += 1
        else:
            dailySchedule.append((tempTime, scheduleInfo.text.split('\n')[0]))  # Store final pair
            count += 1
    fullParsedSchedule.append((name, dailySchedule))


""" Used for all villagers
    ->checks for a good constructed schedule (with tables)
    ->checks for a lazy one (just text) or non scheduled villagers"""
def parseSchedule(soup):
    dailySchedule.clear()
    fullParsedSchedule.clear()
    """ First we try to get the table info """
    numTables = soup.find_all('table', attrs={'class': 'mw-collapsible'})

    for day in numTables:
        # Try to get the name of the "season"
        name = day.find('span', attrs={'style': 'display:inline; margin-right:0;'})
        """ If this .find() works, then the table is a fullSchedule
            If it fails, it could still be 2 other types of schedule (weak or text)"""
        if name is not None:
            """
            Since we know that we're parsing a full Schedule: 
                parsedSchedule will contain: ('season_name', [dailySchedules])
                    where a dailySchedule is: ('day_type', [(times, locations)])
            """
            parseFullSchedule(name, day)
        else:
            name = day.find('th', attrs={'colspan': '2'})
            """ If this .find() works, we're working with a weakSchedule
                If it fails, it can be text based schedule or simply not have one"""
            if name is not None:
                """
                Since we know that we're parsing a weak Schedule: 
                    parsedSchedule will contain: [('day_type', (times, locations))]
                """
                parseWeakSchedule(name, day)

    """ After checking for well constructed schedules, we check if the villager should have one """
    scheduled = soup.find('span', attrs={'id': 'Schedule', 'class': 'mw-headline'})
    if scheduled is None:
        # If they shouldn't have a schedule, this message "is" their schedule
        fullParsedSchedule.append("I'm sorry, this person doesn't have a schedule")
    elif len(fullParsedSchedule) == 0:
        """ If it hasn't been setup already, their schedule is text based
            Since we know that we're parsing a text Schedule: 
                parsedSchedule will contain: ['schedule']
        """
        name = soup.find('span', attrs={'id': 'Schedule', 'class': 'mw-headline'})
        fullParsedSchedule.append(name.find_next('p').text.split('\n')[0])


class ScrapSchedule(object):
    def __init__(self) -> None:
        self.data = None
        self.url = "https://stardewvalleywiki.com/"

    def getWebByVillager(self, villager):
        httppool = urllib3.PoolManager()

        url_villager = self.url + villager.name
        resposta = httppool.request("GET", url_villager)

        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        # regex = re.compile(".*wikitable.*")
        soup = bs4.BeautifulSoup(self.html, features="html.parser")
        parseSchedule(soup)
        self.data = fullParsedSchedule

    def extract_data(self):
        self.data = self.data

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def get_data(self, villager):
        self.getWebByVillager(villager)
        self.parse_html()
        return self.data


if __name__ == "__main__":  # for testing purposes
    client = ScrapSchedule()
    # testing that, for all villagers, we get what is expected
    vills = ['Alex', 'Elliott', 'Harvey', 'Sam', 'Sebastian', 'Shane', 'Abigail', 'Emily', 'Haley', 'Leah', 'Maru',
             'Penny',
             'Caroline', 'Clint', 'Demetrius', 'Dwarf', 'Evelyn', 'George', 'Gus', 'Jas', 'Jodi', 'Kent', 'Krobus',
             'Leo', 'Lewis',
             'Linus', 'Marnie', 'Pam', 'Pierre', 'Robin', 'Sandy', 'Vincent', 'Willy', 'Wizard', 'Birdie', 'Bouncer',
             'Gil',
             'Governor', 'Grandpa', 'Gunther', 'Henchman', 'Marlon', 'Morris', 'Mr. Qi', 'Professor_Snail']
    for i in vills:
        vill = Villager()
        vill.name = i
        print("Villager: " + i)
        dades = client.get_data(vill)
        print(dades)
