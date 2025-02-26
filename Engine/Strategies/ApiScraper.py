import requests
from Engine.Context.ScrapingStrategy import ScrapingStrategy


class ApiScraper(ScrapingStrategy):
    
    def scrape(self, url: str):
        response = requests.get(url + "/api/products")
        data = response.json()
        return [{"product_name": item["name"], "price": item["price"]} for item in data["products"]]
