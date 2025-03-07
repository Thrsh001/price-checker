import re

from Infrastructure.Models import Shop
from Engine.Context.ScrapingStrategy import ScrapingStrategy
from typing import Any, Self


class ScraperContext:

    def __init__(
            self,
            product_name: str,
            url: str = None,
            shop: Shop = None,
            scraper: ScrapingStrategy = None,
            product_data: dict = None
            ) -> None:
        self.product_name: str = product_name
        self.url: str = url
        self.shop = shop
        self.scraper: ScrapingStrategy = scraper
        self.product_data: dict[Any, Any] = product_data

    def set_shop(self, shop: dict) -> Self:
        self.shop = shop
        return self

    def get_shop(self) -> dict:
        return self.shop

    def set_url(self, url: str) -> Self:
        self.url = url
        return self

    def get_url(self) -> str:
        return self.url

    def set_scraper(self, scraper) -> Self:
        self.scraper = scraper
        return self

    def get_scraper(self) -> ScrapingStrategy:
        return self.scraper

    def set_product_data(self, product_data: dict) -> Self:
        """Set product data after cleaning the price."""
        # Clean the price before setting the product data
        if 'price' in product_data:
            product_data['price'] = self.clean_price(product_data['price'])
        self.product_data = product_data
        return self

    def get_product_data(self) -> dict:
        return self.product_data

    def get_product_name(self) -> str:
        return self.product_name

    @staticmethod
    def clean_price(price_str: str) -> float:
        """Remove non-numeric characters and convert the price string to a float."""
        # Remove currency symbols and commas (you can extend this list if needed)
        cleaned_price = re.sub(r'[^\d.]+', '', price_str)
        try:
            return float(cleaned_price)
        except ValueError:
            raise ValueError(f"Invalid price format: {price_str}")