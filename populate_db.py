from typing import List, Dict, Any
from DependencyInjector import DependencyInjector
from Service.Logger import Logger

def populate_shops(db, logger: Logger, shops: List[Dict[str, Any]]) -> None:
    for shop in shops:
        try:
            if db.does_shop_exist(shop["name"]):
                logger.log(f"Shop '{shop['name']}' already exists. Skipping.")
            else:
                db.add_shop(shop["name"], shop["strategy"], shop["url"])
                logger.log(f"Added shop: {shop['name']}")
        except Exception as e:
            logger.log(f"Error adding shop '{shop['name']}': {e}")

def populate_products(db, logger: Logger, products: List[Dict[str, Any]]) -> None:
    for product in products:
        try:
            if not db.does_shop_exist(product["shop"]):
                logger.log(f"Shop '{product['shop']}' does not exist. Cannot add product '{product['name']}'.")
                continue
            db.save_record(product["name"], product["price"], product["shop"])
            logger.log(f"Added product: {product['name']} for shop '{product['shop']}'")
        except Exception as e:
            logger.log(f"Error adding product '{product['name']}': {e}")

def main() -> None:
    db = DependencyInjector.get_db()
    logger = DependencyInjector.get_logger()

    # Example shop data
    shops: List[Dict[str, str]] = [
        {
            "name": "ShopA",
            "strategy": "ShopAStrategy",
            "url": "https://shopa.com/search?q={keyword}"
        },
        {
            "name": "ShopB",
            "strategy": "ShopBStrategy",
            "url": "https://shopb.com/products?search={keyword}"
        },
        # Add more shops as needed
    ]

    # Example product data (optional)
    products: List[Dict[str, Any]] = [
        {
            "name": "Example Product 1",
            "price": 19.99,
            "shop": "ShopA"
        },
        {
            "name": "Example Product 2",
            "price": 29.99,
            "shop": "ShopB"
        },
        # Add more products as needed
    ]

    try:
        logger.log("Populating shops...")
        populate_shops(db, logger, shops)
        logger.log("Populating products...")
        populate_products(db, logger, products)
    except Exception as e:
        logger.log(f"Unexpected error during population: {e}")
    finally:
        db.close()
        logger.log("Database session closed.")

if __name__ == "__main__":
    main()
