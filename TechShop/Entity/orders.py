from Entity.customers import Customers

class Orders:
    def __init__(self, order_id, customer: Customers, order_date, total_amount=0.0):
        self.__order_id = order_id
        self.__customer = customer  # Composition
        self.__order_date = order_date
        self.__total_amount = total_amount

    @property
    def order_id(self):
        return self.__order_id

    @property
    def customer(self):
        return self.__customer

    @property
    def order_date(self):
        return self.__order_date

    @order_date.setter
    def order_date(self, value):
        self.__order_date = value

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        if value < 0:
            raise ValueError("Total amount must be non-negative")
        self.__total_amount = value

    def get_order_details(self):
        return f"OrderID: {self.__order_id}, Customer: {self.__customer.get_customer_details()}, Amount: ₹{self.__total_amount}"
