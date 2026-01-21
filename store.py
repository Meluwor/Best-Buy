from typing import List

from products import Product


class Store:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.list_of_products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list) -> float:
        total = 0.0
        # im not sure if the order should stop if a product 'amount' isn't available
        # atm just products which are stored in the proper amount will be regarded
        for product, amount in shopping_list:
            # there could be products which are not added to this store
            if product not in self.list_of_products:
                continue
            try:
                total += product.buy(amount)
            except ValueError as e:
                print(f'For Product {product.name} ', e)
        self.list_of_products = self.get_all_products()
        return total
