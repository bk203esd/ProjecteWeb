import urllib3
import bs4
from stardewApp.models import Villager


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
        soup = bs4.BeautifulSoup(self.html, features="html.parser")

        table_schedule = soup.find('table', attrs={'class': 'mw-collapsible'})

        self.data = []
        print(table_schedule)

    def extract_data(self):
        self.data = self.data

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def get_data(self, villager):
        self.getWebByVillager(villager)
        self.parse_html()
        return self.data
