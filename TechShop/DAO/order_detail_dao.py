from Util.db_conn_util import DBConnUtil
from Entity.order_details import OrderDetails

class OrderDetailDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def insert_order_detail(self, detail: OrderDetails):
        sql = "INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)"
        data = (
            detail.order_detail_id,
            detail.order.order_id,
            detail.product.product_id,
            detail.quantity
        )
        self.cursor.execute(sql, data)
        self.conn.commit()
