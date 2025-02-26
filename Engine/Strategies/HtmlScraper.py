import requests
from bs4 import BeautifulSoup
from Engine.Context.ScrapingStrategy import ScrapingStrategy


class HtmlScraper(ScrapingStrategy):

    def scrape(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        product_name = soup.find("h1", {"class": "product-title"}).text.strip()
        price = soup.find("span", {"class": "price"}).text.strip()
        return {"product_name": product_name, "price": price}
