from playwright.sync_api import sync_playwright
from Engine.Context.ScrapingStrategy import ScrapingStrategy
from Engine.Context.ScraperContext import ScraperContext
import time


class PlaywrightScraper(ScrapingStrategy):

    def __init__(self):
        super().__init__()

    def scrape(self, url: str, product: str):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(url)
            # time.sleep(10)

            price = page.query_selector(".product-price").inner_text()

            browser.close()
            return {"product_name": product, "price": price}
        
