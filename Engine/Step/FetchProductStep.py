class FetchProductStep:
    
    def __init__(self, scraper):
        self.scraper = scraper

    def execute(self, url):
        return self.scraper.scrape(url)