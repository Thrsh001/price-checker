import argparse
from DependencyInjector import DependencyInjector
from Engine.Context.ScraperContext import ScraperContext

def main():
    parser = argparse.ArgumentParser(description="Price comparison scraper.")
    parser.add_argument("-p", "--product", required=True, help="Product to search for.")
    parser.add_argument("-s", "--shop", required=True, help="Shop to scrape from.")
    args = parser.parse_args()

    db = DependencyInjector.get_db()
    logger = DependencyInjector.get_logger()

    shop = db.get_shop(args.shop)
    if not shop:
        logger.log(f"Shop {args.shop} not found in database.")
        return

    context = ScraperContext(args.product)
    scraper = DependencyInjector.get_scraper(shop["strategy"])
    url = shop["url"] + args.product

    logger.log(f"Starting scrape for {args.product} from {args.shop}...")

    product_data = scraper.scrape(url, args.product)
    print(product_data)
    exit()


    product_dto = DependencyInjector.get_product_dto(
        product_data["name"], product_data["price"]
    )
    db.save({"name": product_dto.name, "price": product_dto.price})
    logger.log("Scraping complete.")

if __name__ == "__main__":
    main()
