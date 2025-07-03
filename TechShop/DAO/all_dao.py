from Util.db_conn_util import DBConnUtil


class ReportDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def get_sales_report(self):
        self.cursor.execute("""
            SELECT p.ProductName, SUM(od.Quantity) AS TotalSold, SUM(od.Quantity * p.Price) AS Revenue
            FROM OrderDetails od
            JOIN Products p ON od.ProductID = p.ProductID
            GROUP BY p.ProductName
        """)
        return self.cursor.fetchall()

class CustomerUpdateDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def update_customer(self, customer_id, new_email, new_phone, new_address):
        sql = "UPDATE Customers SET Email=%s, Phone=%s, Address=%s WHERE CustomerID=%s"
        self.cursor.execute(sql, (new_email, new_phone, new_address, customer_id))
        self.conn.commit()

class PaymentDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def record_payment(self, payment_id, order_id, method, amount):
        sql = "INSERT INTO Payments (PaymentID, OrderID, PaymentMethod, Amount) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (payment_id, order_id, method, amount))
        self.conn.commit()

class ProductSearchDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def search_products(self, keyword):
        like_pattern = f"%{keyword}%"
        sql = "SELECT * FROM Products WHERE ProductName LIKE %s OR Description LIKE %s"
        self.cursor.execute(sql, (like_pattern, like_pattern))
        return self.cursor.fetchall()