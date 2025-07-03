import mysql.connector

class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided."):
        super().__init__(message)

class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available."):
        super().__init__(message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Order details are incomplete."):
        super().__init__(message)

class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed."):
        super().__init__(message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection error."):
        super().__init__(message)

class ConcurrencyException(Exception):
    def __init__(self, message="Concurrent update conflict detected."):
        super().__init__(message)

class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed."):
        super().__init__(message)

class AuthorizationException(Exception):
    def __init__(self, message="Unauthorized access."):
        super().__init__(message)