from Util.db_conn_util import DBConnUtil
from CustomException.custom_exceptions import InvalidDataException
from Util.db_property_util import DBPropertyUtil
class CustomerDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def is_email_exists(self, email):
        self.cursor.execute("SELECT 1 FROM Customers WHERE Email=%s", (email,))
        return self.cursor.fetchone() is not None

    def insert_customer(self, customer):
        if self.is_email_exists(customer.email):
            raise InvalidDataException("Email already exists.")

        sql = "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (customer.customer_id, customer.first_name, customer.last_name, customer.email, customer.phone, customer.address)
        self.cursor.execute(sql, data)
        self.conn.commit()
