from promotions import Promotions


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_promotion(self) -> Promotions:
        return self.promotion

    def set_promotion(self, promotion: Promotions):
        self.promotion = promotion

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: Non-stocked"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.maximum:
            raise ValueError("Quantity exceeds the maximum allowed limit.")

        total_price = self.price * quantity
        return total_price

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity Limit: {self.maximum}"
