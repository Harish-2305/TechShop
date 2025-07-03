from Entity.orders import Orders
from Entity.products import Products

class OrderDetails:
    def __init__(self, order_detail_id, order: Orders, product: Products, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.quantity = quantity  # calls setter

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity must be a positive integer")
        self.__quantity = value

    def calculate_subtotal(self):
        return self.__quantity * self.__product.price
