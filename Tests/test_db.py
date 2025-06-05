import pytest
from DependencyInjector import DependencyInjector

@pytest.fixture
def db():
    db_instance = DependencyInjector.get_db()
    yield db_instance
    db_instance.close()

def test_add_and_check_shop(db):
    shop_name = "TestShop"
    db.add_shop(shop_name, "TestStrategy", "http://example.com/{keyword}")
    assert db.does_shop_exist(shop_name)

def test_save_and_retrieve_product(db):
    shop_name = "TestShop2"
    db.add_shop(shop_name, "TestStrategy", "http://example.com/{keyword}")
    db.save_record("TestProduct", 42.0, shop_name)
    # You could add more checks here if you have a method to retrieve products
