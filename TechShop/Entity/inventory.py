from Entity.products import Products

class Inventory:
    def __init__(self, inventory_id, product: Products, quantity_in_stock, last_stock_update):
        self.__inventory_id = inventory_id
        self.__product = product  # Composition
        self.quantity_in_stock = quantity_in_stock  # uses setter
        self.__last_stock_update = last_stock_update

    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def product(self):
        return self.__product

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        if value < 0:
            raise ValueError("Quantity in stock must be non-negative")
        self.__quantity_in_stock = value

    @property
    def last_stock_update(self):
        return self.__last_stock_update

    def add_to_inventory(self, qty):
        if qty <= 0:
            raise ValueError("Add quantity must be positive")
        self.__quantity_in_stock += qty

    def remove_from_inventory(self, qty):
        if qty > self.__quantity_in_stock:
            raise Exception("Insufficient stock")
        self.__quantity_in_stock -= qty
