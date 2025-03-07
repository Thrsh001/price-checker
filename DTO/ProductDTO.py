class ProductDTO:

    def __init__(self, name: str, price: float, shop: str) -> None:
        self.name = name
        self.price = price
        self.shop = shop

    def __repr__(self):
        return f"ProductDTO(name={self.name}, price={self.price}, shop={self.shop})"
