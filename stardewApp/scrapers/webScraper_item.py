import requests
import urllib3
import bs4


class item(object):
    def __init__(self, name, locations, season):
        self.locations = []
        self.name = name
        self.locations = locations
        self.season = season

    def print_item(self):
        print(self.name, self.locations, self.season)

class ForageScrape(object):
    def __init__(self) -> None:
        self.html = None
        self.url = "https://stardewvalleywiki.com/Foraging"
        self.soup = None

    def get_web(self):
        resposta = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(resposta.content, "html.parser")

    def parse_items(self):
        forageables = {}
        name = "a"
        self.get_web()
        tables = self.soup.select("table:nth-of-type(n+4):nth-of-type(-n+12)")
        num_taula = 0

        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                locations = []
                for cell in cells:
                    if cell.find("a") is not None and cell.find("a").has_attr("href") and cell.find("a").has_attr("title") and cell is cells[1]:
                        name = cell.find("a")["title"]
                        href = cell.find("a")["href"]
                        if name == "Fiddlehead Fern":
                            locations.append("Secret Woods")
                    if cell.find('ul') is not None and cell.find('ul').find('li') and cell is cells[3] and num_taula < 5:
                        loc_elements = cell.find_all('li')
                        for location in loc_elements:
                            title = location.find('a').get_text()
                            locations.append(title)
                    elif num_taula == 5:
                        locations = ["The Beach"]
                    elif num_taula == 6:
                        locations = ["The Mines"]
                    elif num_taula == 7:
                        locations = ["The Desert"]
                    elif num_taula == 8:
                        locations = ["Ginger Island"]

                    if (num_taula == 1):
                        season = "Spring"
                    elif (num_taula == 2):
                        season = "Summer"
                    elif (num_taula == 3):
                        season = "Fall"
                    elif (num_taula == 4):
                        season = "Winter"
                    else:
                        season = "Any"

                    newItem = item(name, locations, season)
                    forageables[name] = newItem

            num_taula += 1
        return forageables


class CookingScrape(object):
    def __init__(self) -> None:
        self.html = None
        self.url = "https://stardewvalleywiki.com/Cooking"
        self.soup = None

    def get_web(self):
        resposta = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(resposta.content, "html.parser")

    def parse_items(self):
        Dishes = {}
        self.get_web()
        tables = self.soup.select("table:nth-of-type(n)")

        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                ingredients = []
                for cell in cells:
                    if cell.find("a") is not None and cell.find("a").has_attr("href") and cell.find("a").has_attr("title") and cell is cells[1]:
                        name = cell.find("a")["title"]
                    if cell.find('ul') is not None and cell.find('ul').find('li') and cell is cells[3]:
                        ing_elements = cell.find_all('li')
                        for ingredient in ing_elements:
                            title = ingredient.find('a').get_text()
                            ingredients.append(title)

                    newItem = item(name, ingredients, "Any")
                    Dishes[name] = newItem

        return Dishes

def main():
    forage = ForageScrape()
    forage_items = forage.parse_items()
    del forage_items["a"]

    for name in forage_items:
        item = forage_items[name]
        item.print_item()

    dish = CookingScrape()
    dishes = dish.parse_items()

    for name in dishes:
        forage_items[name].print_item()

if __name__ == "__main__":
    main()
