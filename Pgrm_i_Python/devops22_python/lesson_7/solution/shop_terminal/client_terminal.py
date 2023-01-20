from product_server import ProductServer


def get_connection():
    return ProductServer()


class Terminal():
    def __init__(self, server):
        self.server = server

    def get_price(self, product_number):
        return self.server.get_price(product_number)


def main():
    terminal = Terminal(get_connection())
    product_number = input("Enter product number:")
    print(f"{product_number} cost {terminal.get_price(product_number)} sek")


if __name__ == '__main__':
    main()
