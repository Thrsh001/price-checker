class ProductReadModel:

    def __init__(self, product):
        self.product = product

    def get_name(self):
        return self.product.name

    def get_price(self):
        return self.product.price
    