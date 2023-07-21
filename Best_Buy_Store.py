import products
import store


def start(store_obj):
    while True:
        print("Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("All products in store:")
            all_products = store_obj.get_all_products()
            for product in all_products:
                print(product.show())

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print("Total amount in store:", total_quantity)

        elif choice == "3":
            product_list = store_obj.get_all_products()
            print("Available products:")
            for index, product in enumerate(product_list, stat=1):
                print(f"{index}. {product.show()}")
            order_list = []
            while True:
                product_choice = input("Enter the product number (0 to finish): ")
                if product_choice == "0":
                    break
                try:
                    product_choice = int(product_choice)
                    if 1 <= product_choice <= len(product_list):
                        product = product_list[product_choice - 1]
                        quantity = input("Enter the quantity: ")
                        try:
                            quantity = int(quantity)
                            order_list.append((product, quantity))
                        except ValueError:
                            print("Invalid quantity. Please enter a number.")
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            total_price = store_obj.order(order_list)
            print("Order placed successfully.")
            print("Total price:", total_price)

        elif choice == "4":
            print("Quitting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store()
    for product in product_list:
        best_buy.add_product(product)

    start(best_buy)


if __name__ == "__main__":
    main()
