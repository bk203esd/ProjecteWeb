import urllib3
import bs4
import re
from stardewApp.models import Villager


# class Villager():
#     def __init__(self, name = "", birthday = "", love = [], like = []) -> None:
#         self.name = name
#         self.birthday = birthday
#         self.love = love
#         self.like = like
#
#     def print(self):
#         print(f'Villager: {self.name}, \n\tBirthdate: {self.birthday}\n\tLoves: {self.love}\n\tLikes: {self.like}')


class WebScrape(object):
    def __init__(self) -> None:
        self.url = "https://stardewvalleywiki.com"

    def get_web(self, sufix):
        httppool = urllib3.PoolManager()

        resposta = httppool.request("GET", self.url + sufix)

        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        soup = bs4.BeautifulSoup(self.html, features="html.parser")
        # print(soup)
        div_main = soup.find_all('div', attrs={'class': 'gallerytext'})
        self.data = []
        for ref in div_main:
            villager = ref.find('a').get('title')
            self.data.append(villager)

    def parse_villager_bs4(self):
        regex = re.compile('^(?=.*wikitable)(?=.*roundedborder)(?!.*mw-made-collapsible)(?!.*mw-collapsible).*')
        soup = bs4.BeautifulSoup(self.html, features='html.parser')
        div_love = soup.find_all('table', attrs={'class': regex})[0]
        lines = []
        love = []

        lines.extend(div_love.find_all('tr')[2:])
        for line in lines:
            love.extend(line.find_all('a')[1])

        div_like = soup.find_all('table', attrs={'class': regex})[1]
        lines = []
        like = []

        lines.extend(div_like.find_all('tr')[2:])

        for line in lines:
            like.extend(line.find_all('a')[1])

        div_main = soup.find_all('td', attrs={'id': 'infoboxdetail'})[0]

        birthDate = div_main.find('a').get('title')

        self.data = {}
        self.data['like'] = like
        self.data['love'] = love
        self.data['birthday'] = birthDate

    def extract_data(self):
        self.data = self.data

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def parse_villager_html(self):
        self.parse_villager_bs4()
        self.extract_data()

    def get_names_data(self):
        self.get_web('/Villagers')
        self.parse_html()
        return self.data

    def get_villager_data(self, villager):
        self.get_web(f'/{villager}')
        self.parse_villager_html()
        return self.data


def fill_dades(villager):
    client = WebScrape()
    dades = client.get_villager_data(villager)
    dbvillager = Villager.objects.create(
        name=villager,
        birthday=dades['birthday'],
        love=dades['loved'],
        like=dades['like']
    )
    return dbvillager

# if __name__ == "__main__":
#     client = WebScrape()
#     villagers = {}
#     dades= client.get_names_data()
#     print(dades)
#     for index, villager in enumerate(dades):
#         if villager != 'Krobus':
#             villagers[villager] = Villager(name=villager)
#         if index > 32: break
#
#     for villager in villagers:
#         print(villager)
#         fill_dades(villager)
#         villagers[villager].print()
