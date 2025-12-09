class BaseAppException(Exception):
    """Base class from which all custom exceptions inherit."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class ValidationException(BaseAppException):
    """
    Raised when invalid data is provided.
    
    Args:
        field (str): Name of the field that is invalid
        reason (str): Explanation of the validation issue
    """
    def __init__(self, field, reason):
        message = f"Validation Error -> Field: '{field}' | Reason: {reason}"
        super().__init__(message)

class NotFoundException(BaseAppException):
    """
    Raised when requested data cannot be found.
    
    Args:
        entity_name (str): Name of the object (Shop, Rental, etc.)
        entity_id (str): The requested ID
    """
    def __init__(self, entity_name, entity_id):
        message = f"Not Found -> {entity_name} with ID '{entity_id}' does not exist."
        super().__init__(message)

class BusinessRuleException(BaseAppException):
    """
    Raised when a business rule is violated.
    
    Args:
        description (str): Description of the violated rule
    """
    def __init__(self, description):
        message = f"Business Rule Violation -> {description}"
        super().__init__(message)
