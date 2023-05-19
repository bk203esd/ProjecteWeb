import re

import urllib3
import bs4

seasons = []


class ScrapSeason(object):
    def __init__(self) -> None:
        self.data = None
        self.url = "https://stardewvalleywiki.com"

    def getWeb(self):
        httppool = urllib3.PoolManager()

        url = self.url + "/Seasons"
        resposta = httppool.request("GET", url)

        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        global seasons
        soup = bs4.BeautifulSoup(self.html, features="html.parser")
        seasonTable = soup.find('table', attrs={'id': 'navbox'})

        for tag in seasonTable.find_all('a'):
            if tag.text != "Seasons":
                seasons.append(tag.text)

    def extract_data(self):
        self.data = seasons

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def get_data(self):
        self.getWeb()
        self.parse_html()
        return self.data


if __name__ == "__main__":  # for testing purposes
    client = ScrapSeason()
    client.get_data()
    print(client.data)
