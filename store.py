from typing import List
from products import Product


class Store:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products:
                total_price += product.buy(quantity)
            else:
                raise ValueError("Product is not available in the store.")
            return total_price
