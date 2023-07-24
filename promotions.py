from abc import ABC, abstractmethod


class Promotions(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotions):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity) -> float:
        regular_price = product.price * quantity
        discounted_price = regular_price - (product.price * quantity) / 2
        return discounted_price


class ThirdOneFree(Promotions):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity) -> float:
        full_sets = quantity // 3
        price_of_full_sets = full_sets * (2 * product.price)
        price_of_remaining_items = (quantity % 3) * product.price
        discounted_price = price_of_full_sets + price_of_remaining_items
        return discounted_price


class PercentDiscount(Promotions):
    def __init__(self, percent):
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        total_price = product.price * quantity
        discount_amount = (total_price * self.percent) / 100
        discounted_price = total_price - discount_amount
        return discounted_price
