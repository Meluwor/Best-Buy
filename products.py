class Product:
    def __init__(self, name, price, quantity):
        if not name.strip():
            raise ValueError("You have to enter a product name!")
        self.name = name
        #I expect that products can be free as well
        if price < 0:
            raise ValueError("You have to enter a positive price!")
        self.price = price
        if quantity < 0:
            raise ValueError("You have to enter a positive quantity!")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False
        else:
            # quantity cant be negative at this point
            self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if self.quantity + quantity < 0:
            raise ValueError("No negative quantity allowed!")
        self.quantity += quantity
        if self.quantity == 0:
            self.set_inactive()
        elif self.quantity > 0:
            self.set_active()

    def is_active(self) -> bool:
        return self.active

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def buy(self, quantity) -> float:
        if quantity < 0:
            raise ValueError("You cant have negative quantity!")
        if self.is_active():
            self.set_quantity(-quantity)
            return self.price * quantity
        raise ValueError(f'No more {self.name} in store')

    def show(self):
        print(f'{self.name}, Price: {self.price}, Quantity: {self.quantity}')


def product_test():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    # an 'empty' product could be one later or not who knows
    mac2: Product | None = None
    try:
        mac2 = Product("Mac", price=1450, quantity=-100)
    except ValueError as e:
        print(f'Something went wrong: {e}')
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    print(mac2)
    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
    try:
        mac.buy(10)
    except ValueError as e:
        print(e)
    print("finished")

def main():
    product_test()

if __name__ == "__main__":
    main()