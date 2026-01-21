class Product:
    def __init__(self, name, price, quantity):
        if not name.strip():
            raise ValueError("You have to enter a product name!")
        self.name = name
        # I expect that products can be free as well
        if price < 0:
            raise ValueError("You have to enter a positive price!")
        self.price = price
        if quantity < 0:
            raise ValueError("You have to enter a positive quantity!")
        self.quantity = quantity
        self.active = self.quantity > 0

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
