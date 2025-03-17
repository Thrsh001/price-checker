from typing import Optional
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from Infrastructure.Models import Shop, Product, Base


load_dotenv()  # Load environment variables from .env


class SingletonClass(object):
  instance = None

  def __new__(cls):
    if not cls.instance:
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance


class DatabaseClient(SingletonClass):
    def __init__(self):
        # Database connection
        database_url = os.getenv("DATABASE_URL")
        engine = create_engine(database_url, echo=True)

        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)

        sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.db = sessionLocal()


    def save_record(self, name: str, price: float, shop_name: str) -> None:
        """Save product info into the database."""
        try:
            shop = self.db.query(Shop).filter_by(name=shop_name).first()
            if not shop:
                raise ValueError(f"Shop '{shop_name}' not found in database.")

            # Create a new product instance and associate it with the shop
            product = Product(name=name, price=price, shop_id=shop.id)

            # Debugging: print the product data before saving
            print(f"Saving product: Name={product.name}, Price={product.price}, Shop={shop.name}")

            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            print(f"Product saved with ID: {product.id}")

        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")
            self.db.rollback()  # Rollback any changes in case of error
        else:
            print("Record saved successfully.")

    def add_shop(self, name, strategy, url) -> None:
        """Add a shop if it does not exist."""
        shop = self.db.query(Shop).filter_by(name=name).first()
        if not shop:
            shop = Shop(name=name, strategy=strategy, url=url)
            self.db.add(shop)
            self.db.commit()
            self.db.refresh(shop)
            print(f"Added shop: {name}")
        else:
            print(f"Shop '{name}' already exists.")

    def update_shop_column(self, shop_name, column, value) -> None:
        """Update any column for an existing shop."""
        shop = self.db.query(Shop).filter_by(name=shop_name).first()
        if shop:
            if hasattr(shop, column):  # Check if the column exists
                setattr(shop, column, value)  # Dynamically set the column value
                self.db.commit()
                print(f"Updated {shop_name}: {column} = {value}")
            else:
                print(f"Column '{column}' does not exist in Shop.")
        else:
            print(f"Shop '{shop_name}' not found.")

            shop.column = column
            self.db.commit()
            print(f"Updated {shop_name} {column} to {value}")

    def get_shop(self, shop_name: str) -> Optional[Shop]:
        """Retrieve a shop by name."""
        return self.db.query(Shop).filter_by(name=shop_name).first()

    def does_shop_exist(self, shop_name: str) -> Optional[Shop]:
        """Check if a shop exists."""
        return self.db.query(Shop).filter_by(name=shop_name).first() is not None

    def get_url(self, shop_name: str, keyword: str) -> str | None:
        """Retrieve the formatted URL for a shop."""
        shop = self.get_shop(shop_name)
        if shop:
            return shop.url.format(keyword=keyword)
        return None

    def close(self) -> None:
        """Close the database session."""
        self.db.close()

