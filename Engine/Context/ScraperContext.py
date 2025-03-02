class ScraperContext:
    
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.url = None
        self.shop = None
        self.product_data = None
        self.scraper = None

    def set_shop(self, shop: dict):
        self.shop = shop
        return self

    def set_url(self, url: str):
        self.url = url
        return self

    def set_scraper(self, scraper):
        self.scraper = scraper
        return self

    def set_product_data(self, product_data: dict):
        self.product_data = product_data
        return self

    def get_product_name(self) -> str:
        return self.product_name

    def get_url(self) -> str:
        return self.url

    def get_shop(self) -> dict:
        return self.shop

    def get_product_data(self) -> dict:
        return self.product_data

    def get_scraper(self):
        return self.scraper