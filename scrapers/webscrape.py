import urllib3
import bs4

class WebScrape(object):
    def __init__(self) -> None:
        self.url = "https://stardewvalleywiki.com/Villagers"
    
    def get_web(self):
        httppool = urllib3.PoolManager()

        resposta = httppool.request("GET", self.url)

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
        

    def extract_data(self):
        self.data = self.data

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def get_data(self):
        self.get_web()
        self.parse_html()
        return self.data
    
if __name__ == "__main__":
    client = WebScrape()
    dades= client.get_data()
    print(dades)