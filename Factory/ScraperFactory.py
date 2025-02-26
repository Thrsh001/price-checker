from Engine.Context.ScraperContext import ScraperContext
from Engine.Strategies.PlaywrightScraper import PlaywrightScraper
from Engine.Strategies.HtmlScraper import HtmlScraper
from Engine.Strategies.ApiScraper import ApiScraper

class ScraperFactory:

    @staticmethod
    def create_scraper(strategy_name) -> ScraperContext:
        if strategy_name == "playwright":
            return ScraperContext(PlaywrightScraper())
        elif strategy_name == "html":
            return ScraperContext(HtmlScraper())
        elif strategy_name == "api":
            return ScraperContext(ApiScraper())
        raise ValueError(f"Strategy {strategy_name} not implemented.")
