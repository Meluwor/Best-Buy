from typing import List

from products import Product


class Store:

    def __init__(self,list_of_products):
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
        #atm just products which are stored in the proper amount will be regarded
        for product, amount in shopping_list:
            #there could be products which are not added to this store
            if product not in self.list_of_products:
                continue
            try:
                total += product.buy(amount)
            except ValueError as e:
                print(f'For Product {product.name} ',e)
        self.list_of_products = self.get_all_products()
        return total

def order_test():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")
    print("order_test() done")

def store_test():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print("best_buy.get_total_quantity() ",best_buy.get_total_quantity())
    print("best_buy.order ",best_buy.order([(products[0], 1), (products[1], 2)]))
    print("store_test() done")

def main():
    order_test()
    store_test()



if __name__ == "__main__":
    main()