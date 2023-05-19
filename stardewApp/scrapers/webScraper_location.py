import urllib3
import bs4

final_locations = []


class ScrapLocation(object):
    def __init__(self) -> None:
        self.url = "https://stardewvalleywiki.com"
        self.data = None

    def get_web(self):
        httppool = urllib3.PoolManager()

        resposta = httppool.request("GET", self.url)

        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        soup = bs4.BeautifulSoup(self.html, features="html.parser")
        all_locations = soup.find_all('div', attrs={'class': 'bordered'})
        self.data = []
        for location in all_locations:
            locations = location.find_all('p')
            for item in locations:
                final_locations.append(item.text.split('\n')[0])
            locations = location.find_all('dl')
            for item in locations:
                final_locations.append(item.text.split('\n')[0])

    def extract_data(self):
        self.data = final_locations

    def parse_html(self):
        self.parse_bs4()
        self.extract_data()

    def get_data(self):
        self.get_web()
        self.parse_html()
        return self.data


if __name__ == "__main__":
    client = ScrapLocation()
    dades = client.get_data()
    print(dades)
