from Engine.Context.ScrapingStrategy import ScrapingStrategy
from Engine.Strategies.PlaywrightScraper import PlaywrightScraper
from Engine.Strategies.HtmlScraper import HtmlScraper
from Engine.Strategies.ApiScraper import ApiScraper

class ScraperFactory:

    @staticmethod
    def create_scraper(strategy_name) -> ScrapingStrategy:
        if strategy_name == "playwright":
            return PlaywrightScraper()
        elif strategy_name == "html":
            return HtmlScraper()
        elif strategy_name == "api":
            return ApiScraper()
        raise ValueError(f"Strategy {strategy_name} not implemented.")
