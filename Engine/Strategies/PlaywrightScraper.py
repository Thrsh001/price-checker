from playwright.sync_api import sync_playwright
from typing import Dict, Any
from Engine.Context.ScrapingStrategy import ScrapingStrategy
import time


class PlaywrightScraper(ScrapingStrategy):

    def __init__(self):
        super().__init__()

    def scrape(self, url: str, product: str) -> Dict[str, Any]: 
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(url)
            # time.sleep(10)

            price = page.query_selector(".product-price").inner_text()

            browser.close()
            return {
                "name": product,
                "price": price
                }
        
