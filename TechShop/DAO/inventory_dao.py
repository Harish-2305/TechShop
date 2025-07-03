from Util.db_conn_util import DBConnUtil
from Entity.inventory import Inventory

class InventoryDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def update_stock(self, product_id, quantity_change):
        sql = "UPDATE Inventory SET QuantityInStock = QuantityInStock + %s WHERE ProductID = %s"
        self.cursor.execute(sql, (quantity_change, product_id))
        self.conn.commit()

    def set_stock(self, inventory_id, product_id, quantity, date):
        sql = "INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (inventory_id, product_id, quantity, date))
        self.conn.commit()

    def delete_inventory_item(self, product_id):
        self.cursor.execute("DELETE FROM Inventory WHERE ProductID = %s", (product_id,))
        self.conn.commit()
