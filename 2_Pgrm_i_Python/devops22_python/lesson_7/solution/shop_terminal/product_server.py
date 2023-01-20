
class ProductServer:

    def __init__(self):
        self.price = {"12345": 100, "111": 200}

    def get_price(self, product_number):
        return self.price[product_number]
