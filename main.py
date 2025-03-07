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

    if not db.does_shop_exists(args.shop):
        logger.log(f"Shop {args.shop} not found in database.")
        return

    # Retrieve shop from database
    shop_name: str = args.shop
    shop = db.get_shop(shop_name)

    print(shop.strategy)

    if shop:
        scraper = DependencyInjector.get_scraper(shop.strategy)
    else:
        raise ValueError ("Shop not found!")

    # Build URL for scraping
    url: str = db.get_url(shop_name, args.product)

    # Create scraper context
    context = ScraperContext(args.product, url, shop, scraper)

    logger.log(f"Starting scrape for {args.product} from {shop_name}...")

    try:
        # Retrieve scraper and perform scraping
        scraper = context.get_scraper()
        if not scraper:
            logger.log("No scraper configured in context")
            return

        product_data = scraper.scrape(
            context.get_url(),
            context.get_product_name()
        )

        context.set_product_data(product_data)

    except Exception as e:
        logger.log(f"An error occurred while trying to scrape: {str(e)}")
        return

    # Create a ProductDTO with the product data
    product_dto = DependencyInjector.get_product_dto(
        product_data["name"], product_data["price"], shop_name
    )
    # Save the product record to the database
    db.save_record(product_dto.name, product_dto.price, shop_name)

    logger.log("Scraping complete.")


if __name__ == "__main__":
    main()
