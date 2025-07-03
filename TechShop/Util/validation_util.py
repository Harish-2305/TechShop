import  re
from CustomException.custom_exceptions import InvalidDataException
class ValidationUtil:
    @staticmethod
    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidDataException("Invalid email format.")