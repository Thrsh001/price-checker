from DependencyInjector import DependencyInjector

def test_get_scraper_returns_strategy():
    scraper = DependencyInjector.get_scraper("playwright")
    assert scraper is not None
    # Check for a method
    assert hasattr(scraper, "scrape")

def test_scraper_scrape_method(monkeypatch):
    # This test assumes you have a dummy or mock scraper for "playwright"
    class DummyScraper:
        def scrape(self, url, product_name):
            return {"name": product_name, "price": 123.45}

    # Monkeypatch the factory to return DummyScraper
    from Factory.ScraperFactory import ScraperFactory
    monkeypatch.setattr(ScraperFactory, "create_scraper", lambda strategy: DummyScraper())

    scraper = DependencyInjector.get_scraper("playwright")
    result = scraper.scrape("http://example.com", "Widget")
    assert result["name"] == "Widget"
    assert result["price"] == 123.45
