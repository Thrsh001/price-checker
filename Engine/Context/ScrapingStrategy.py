from abc import ABC, abstractmethod
from Engine.Context.ScraperContext import ScraperContext


class ScrapingStrategy(ABC):

    @abstractmethod
    def scrape(self, url: str, product: str):
        pass
