from Util.db_conn_util import DBConnUtil
from Entity.orders import Orders

class OrderDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def insert_order(self, order_id, customer_id, order_date, total_amount):
        sql = "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (order_id, customer_id, order_date, total_amount))
        self.conn.commit()

    def insert_order_detail(self, order_detail_id, order_id, product_id, quantity):
        sql = "INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (order_detail_id, order_id, product_id, quantity))
        self.conn.commit()

    def get_order_status(self, order_id):
        self.cursor.execute("SELECT * FROM Orders WHERE OrderID = %s", (order_id,))
        return self.cursor.fetchone()
