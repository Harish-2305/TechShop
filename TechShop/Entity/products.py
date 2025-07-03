class Products:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.price = price  # call setter


    @property
    def product_id(self):
        return self.__product_id


    @property
    def product_name(self):
        return self.__product_name


    @product_name.setter
    def product_name(self, value):
        self.__product_name = value


    @property
    def description(self):
        return self.__description


    @description.setter
    def description(self, value):
        self.__description = value


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self.__price = value


    def get_product_details(self):
        return f"{self.__product_name}: {self.__description} - Rs.{self.__price}"