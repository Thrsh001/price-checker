from Engine.Context.ScrapingStrategy import ScrapingStrategy
from Factory.ScraperFactory import ScraperFactory
from Infrastructure.Database import Database
from Service.Logger import Logger
from DTO.ProductDTO import ProductDTO


class DependencyInjector:

    @staticmethod
    def get_scraper(strategy: str) -> ScrapingStrategy:
        return ScraperFactory.create_scraper(strategy)

    @staticmethod
    def get_db() -> Database:
        return Database()

    @staticmethod
    def get_logger() -> Logger:
        return Logger()

    @staticmethod
    def get_product_dto(name: str, price: float, shop: str) -> ProductDTO:
        return ProductDTO(name, price, shop)