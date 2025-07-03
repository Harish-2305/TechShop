

import mysql.connector
import re

from Entity.customers import Customers
from Entity.products import Products
from DAO.customer_dao import CustomerDAO
from DAO.product_dao import ProductDAO
from DAO.order_dao import OrderDAO
from DAO.inventory_dao import InventoryDAO
from DAO.all_dao import (
    ReportDAO,
    CustomerUpdateDAO,
    PaymentDAO,
    ProductSearchDAO
)
from Util.validation_util import ValidationUtil
from CustomException.custom_exceptions import InvalidDataException

while True:
    print("=== Welcome to TechShop Management System ===")
    print("1. Customer Registration")
    print("2. Product Catalog Management")
    print("3. Place Order")
    print("4. Track Order Status")
    print("5. Inventory Management")
    print("6. Sales Reporting")
    print("7. Update Customer Account")
    print("8. Payment Processing")
    print("9. Product Search & Recommendations")
    print("0. Exit")

    choice = input("Enter your choice (1–9): ")

    try:
        if choice == '1':
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            ValidationUtil.validate_email(email)
            customer = Customers(1001, fname, lname, email, phone, address)
            dao = CustomerDAO()
            dao.insert_customer(customer)
            print("Registration successful!")

        elif choice == '2':
            pid = int(input("Enter Product ID: "))
            pname = input("Enter Product Name: ")
            desc = input("Enter Description: ")
            price = float(input("Enter Price: "))
            if price < 0:
                raise InvalidDataException("Price must be non-negative.")
            product = Products(pid, pname, desc, price)
            dao = ProductDAO()
            existing = dao.get_product_by_id(pid)
            if existing:
                dao.update_product(product)
                print(" Product updated successfully!")
            else:
                dao.insert_product(product)
                print(" Product added successfully!")

        elif choice == '3':
            print(" Place Order")
            order_dao = OrderDAO()
            order_id = int(input("Enter Order ID: "))
            customer_id = int(input("Enter Customer ID: "))
            order_date = input("Enter Order Date (YYYY-MM-DD): ")
            total = float(input("Enter Total Amount: "))
            order_dao.insert_order(order_id, customer_id, order_date, total)
            detail_id = int(input("Enter Order Detail ID: "))
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            order_dao.insert_order_detail(detail_id, order_id, product_id, quantity)
            inventory_dao = InventoryDAO()
            inventory_dao.update_stock(product_id, -quantity)
            print(" Order placed and inventory updated!")

        elif choice == '4':
            print(" Track Order Status")
            order_id = int(input("Enter Order ID: "))
            dao = OrderDAO()
            order = dao.get_order_status(order_id)
            print(" Order Status:", order)

        elif choice == '5':
            print(" Inventory Management")
            inv_dao = InventoryDAO()
            inv_id = int(input("Enter Inventory ID: "))
            prod_id = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            inv_dao.set_stock(inv_id, prod_id, qty, date)
            print(" Inventory record added!")

        elif choice == '6':
            print(" Sales Reporting")
            report_dao = ReportDAO()
            report = report_dao.get_sales_report()
            for row in report:
                print(f"Product: {row[0]}, Sold: {row[1]}, Revenue: ₹{row[2]}")

        elif choice == '7':
            print(" Update Customer Account")
            cid = int(input("Enter Customer ID: "))
            new_email = input("Enter new Email: ")
            new_phone = input("Enter new Phone: ")
            new_address = input("Enter new Address: ")
            update_dao = CustomerUpdateDAO()
            update_dao.update_customer(cid, new_email, new_phone, new_address)
            print(" Customer updated!")

        elif choice == '8':
            print(" Payment Processing")
            pay_dao = PaymentDAO()
            pay_id = int(input("Enter Payment ID: "))
            ord_id = int(input("Enter Order ID: "))
            method = input("Enter Payment Method: ")
            amt = float(input("Enter Amount: "))
            pay_dao.record_payment(pay_id, ord_id, method, amt)
            print(" Payment recorded!")

        elif choice == '9':
            print(" Product Search & Recommendations")
            keyword = input("Enter product keyword: ")
            search_dao = ProductSearchDAO()
            results = search_dao.search_products(keyword)
            for product in results:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: ₹{product[3]}")

        elif choice == '0':
            print("Thank You !")
            break

        else:
            print("Invalid ! option selected.")


    except InvalidDataException as e:
        print(" Error:", e)
    except Exception as e:
        print(" Something went wrong:", e)
