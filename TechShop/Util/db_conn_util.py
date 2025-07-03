import mysql.connector
from Util.db_property_util import DBPropertyUtil
class DBConnUtil:
    @staticmethod
    def get_connection():
        props = DBPropertyUtil.get_connection_props()
        return mysql.connector.connect(**props)