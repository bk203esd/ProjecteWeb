import requests
import urllib3
import bs4


class item(object):
    def __init__(self, name, location, season, current_url, href):
        self.name = name
        self.locations = location
        self.season = season
        self.href = href
        self.url = current_url + href


class ForageScrape(object):
    def __init__(self) -> None:
        self.html = None
        self.url = "https://stardewvalleywiki.com/Foraging"
        self.soup = None

    def get_web(self):
        resposta = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(resposta.content, "html.parser")

    def parse_items(self):
        self.get_web()
        tables = self.soup.select("table:nth-of-type(n+4):nth-of-type(-n+12)")

        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                for cell in cells:
                    if cell.find("a") is not None and cell.find("a").has_attr("href") and cell.find("a").has_attr("title") and cell is cells[1]:
                        name = cell.find("a")["title"]
                        href = cell.find("a")["href"]
                        print(name, href)
                    if cell.find("ul") is not None and cell.find("ul").has_attr("li") and cell is cells[3]:
                        loc_elements = cell.find_all("li")
                        locations = []
                        for location in loc_elements:
                            title = location.get_text()
                            locations.append(title)
                        print(locations)


class FishingScrape(object):
    def __init__(self) -> None:
        self.html = None
        self.url = "https://stardewvalleywiki.com/Fish"

    def get_web(self):
        httppool = urllib3.PoolManager()
        resposta = httppool.request("GET", self.url)
        self.html = resposta.data.decode("utf-8")

    def get_inf(self):
        algoalgo = "todo"


def main():
    forage = ForageScrape()
    forage.parse_items()


if __name__ == "__main__":
    main()
