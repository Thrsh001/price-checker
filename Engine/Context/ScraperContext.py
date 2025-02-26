# CREATE SCRAPER OBJECT DA GA PROSLEDIM NA STRATEGIJE

# TODO PROMENI 

class ScraperContext:
    
    def __init__(self, strategy):
        self.strategy = strategy

    def scrape(self, url: str, product: str):
        return self.strategy.scrape(url, product)
