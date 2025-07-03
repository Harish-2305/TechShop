class ProductDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def insert_product(self, product):
        sql = "INSERT INTO Products (ProductID, ProductName, Description, Price) VALUES (%s, %s, %s, %s)"
        data = (product.product_id, product.product_name, product.description, product.price)
        self.cursor.execute(sql, data)
        self.conn.commit()

    def update_product(self, product):
        sql = "UPDATE Products SET ProductName=%s, Description=%s, Price=%s WHERE ProductID=%s"
        data = (product.product_name, product.description, product.price, product.product_id)
        self.cursor.execute(sql, data)
        self.conn.commit()

    def get_product_by_id(self, product_id):
        self.cursor.execute("SELECT * FROM Products WHERE ProductID = %s", (product_id,))
        return self.cursor.fetchone()
