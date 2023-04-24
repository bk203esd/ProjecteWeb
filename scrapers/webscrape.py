import urllib3
import bs4

class Villager():
    def __init__(self, name = "", birthday = "", love = [], like = []) -> None:
        self.name = name
        self.birthday = birthday
        self.love = love
        self.like = like


class WebScrape(object):
    def __init__(self) -> None:
        self.url = "https://stardewvalleywiki.com"
    
    def get_web(self, sufix):
        httppool = urllib3.PoolManager()

        resposta = httppool.request("GET", self.url + sufix)

        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        soup = bs4.BeautifulSoup(self.html, features = "html.parser")
        #print(soup)
        div_main = soup.find_all('div', attrs={'class':'gallerytext'})
        #self.data = div_main.find_all('title')
        self.data = []
        for ref in div_main:
            villager = ref.find('a').get('title')
            self.data.append(villager)

    def parse_villager_bs4(self):
        soup = bs4.BeautifulSoup(self.html, features = 'html.parser')
        div_like = soup.find_all('table', attrs={'class':'wikitable roundedborder'})[0:2]
        for ref in div_like[0]:
            lines = ref.find_all_next('tr')[2:]
            for line in lines:
                like = line.find_all_next('td')[1].get('title')
                print(like)

        self.data = {}
        self.data['like'] = []
        self.data['love'] = []
        self.data['birthday'] = ''
        print(tr)
        
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
    
if __name__ == "__main__":
    client = WebScrape()
    villagers = {}
    dades= client.get_names_data()
    for villager in dades:
        villagers[villager] = Villager(name=villager)
    for villager in villagers:
        print(villager)
        fill_dades(villager)
    print(dades)