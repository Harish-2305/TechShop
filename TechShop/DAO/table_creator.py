from Util.db_conn_util import DBConnUtil

class TableCreator:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                CustomerID INT PRIMARY KEY,
                FirstName VARCHAR(100),
                LastName VARCHAR(100),
                Email VARCHAR(100),
                Phone VARCHAR(20),
                Address VARCHAR(255)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                ProductID INT PRIMARY KEY,
                ProductName VARCHAR(100),
                Description TEXT,
                Price DECIMAL(10,2)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                OrderID INT PRIMARY KEY,
                CustomerID INT,
                OrderDate DATE,
                TotalAmount DECIMAL(10,2),
                FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrderDetails (
                OrderDetailID INT PRIMARY KEY,
                OrderID INT,
                ProductID INT,
                Quantity INT,
                FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
                FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Inventory (
                InventoryID INT PRIMARY KEY,
                ProductID INT,
                QuantityInStock INT,
                LastStockUpdate DATE,
                FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
            )
        """)

        self.conn.commit()
        print("Customer table created.")
