from abc import ABC, abstractmethod
from typing import Dict, Any


class ScrapingStrategy(ABC):

    @abstractmethod
    def scrape(self, url: str, product: str) -> Dict[str, Any]:
        pass
