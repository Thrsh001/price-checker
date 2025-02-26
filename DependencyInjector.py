from Factory.ScraperFactory import ScraperFactory
from Infrastructure.Database import Database
from Service.Logger import Logger
from DTO.ProductDTO import ProductDTO


class DependencyInjector:

    @staticmethod
    def get_scraper(strategy):
        return ScraperFactory.create_scraper(strategy)

    @staticmethod
    def get_db():
        return Database()

    @staticmethod
    def get_logger():
        return Logger()

    @staticmethod
    def get_product_dto(name, price):
        return ProductDTO(name, price)