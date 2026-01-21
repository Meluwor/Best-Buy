from matplotlib.style.core import available

from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = Store(product_list)

def get_main_menu_options():
    """
    All atm available menu options.
    """
    return ["List all products in store","Show total amount in store","Make an order","Quit"]

def print_options(some_list):
    """
    This function will print a given list to screen like 1. list_entry[0]  2. list_entry[1] etc
    """
    for i, value in enumerate(some_list):
        print(f'{i+1}. {value}')


def start():
    print("   Store Menu")
    print("   ----------")
    print_options(get_main_menu_options())


def get_number_from_user(option_length, text, allow_empty):
    """
    This function shall ensure to get an int value from the user based on the current options.
    """
    while True:
        user_input = input(text).strip()
        if allow_empty and not user_input:
            print()
            break
        try:
            user_input = int(user_input)
            if 1 <= user_input <= option_length:
                return user_input
            else:
                print(f'Please Enter a number (1-{option_length})')
        except ValueError:
            print(f'Please Enter a number (1-{option_length})')


def list_all_products():
    """
    This function will list all available products.
    """
    for i ,product in enumerate(best_buy.get_all_products()):
        print(f'{i+1} ', end = "")
        product.show()
    print()

def show_total_amount():
    print(f'Total of {best_buy.get_total_quantity()} items in store')
    print()


def order_products():
    """
    This function shall ensure the user to make an order of all available products.
    """
    price = 0
    while True:
        available_products = best_buy.get_all_products()
        #if the store is empty no more orders can be made
        if not available_products:
            print("Sold out")
            break
        # the demo just show the available products once
        # I show them after each oder so the user knows the available amount
        list_all_products()
        order_list = []
        text = ("When you want to finish order, enter empty text.\n"
                "Which product do you want? ")
        user_input = get_number_from_user(len(available_products),text,True)
        #the demo ask for an amount even when the user used an empty input which should finish the order
        if not user_input:
            break
        product_to_order = available_products[user_input-1]
        text = "What amount do you want? "
        #the user can just order amounts which are available
        #im not sure if the user shall be able to enter unavailable amounts like he can do in the demo
        #sure its says there are not enough after he ordered  but why should he be able to do so if he cant even get it
        amount_of_products = get_number_from_user(product_to_order.get_quantity(),text,False)
        order_list.append((product_to_order,amount_of_products))
        price += best_buy.order(order_list)
        #not sure how the demo handle this because of 'Product added to list' which prolly causes
        # the problem with amounts like order 1000 when just 200 in store
        print("Product ordered!")
        print()
    if price > 0:
        print(f'All orders made! Total payment: ${price}')
    print()


def handle_main_menu(user_input):
    """
    This function will handle most of the main menu options.
    """
    if user_input == 1:
        list_all_products()
    elif user_input == 2:
        show_total_amount()
    elif user_input == 3:
        order_products()


def main():
    menu_length = len(get_main_menu_options())
    while True:
        start()
        user_input = get_number_from_user(menu_length, "Please choose a number: ",False)
        if user_input == menu_length:
            break
        handle_main_menu(user_input)


if __name__ == "__main__":
    main()