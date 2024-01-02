import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, stock: str):
        self.stock = stock.strip().lower()
        self.url = 'https://ticker.finology.in/company/' + stock
        
    def getPage(self):
        self.page = requests.get(self.url)
        return self.page
     
    def getPrice(self):
        try:
            page = self.getPage()
            beautifulsoup = BeautifulSoup(page._content, 'html.parser')

            # print(soup)
            result = {}
            result['price'] = float(beautifulsoup.find("span", {"class": "currprice"}).find("span",{"class": "Number"}).text)
            return result
        except Exception as e:
            return "Unable to Fetch"
        


if __name__ == "__main__":
    sail = Scrapper('SAIL')
    print(sail.getPrice())