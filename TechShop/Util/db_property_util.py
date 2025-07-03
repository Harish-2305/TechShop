import mysql.connector
class DBPropertyUtil:
    @staticmethod
    def get_connection_props():
        return {
            'host': 'localhost',
            'user': 'root',
            'password': '230524',
            'database': 'TechShopDB'
        }