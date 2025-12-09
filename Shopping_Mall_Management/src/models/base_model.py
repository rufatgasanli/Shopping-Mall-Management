from abc import ABC, abstractmethod

class BaseModel(ABC):
    """
    Abstract Base Class.
    OOP Principles: Abstraction, Inheritance.
    All models must inherit from this class.
    """

    @abstractmethod
    def to_dict(self):
        """Method to convert the object into a dictionary. Must be implemented."""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        """Method to create an object from a dictionary. Must be implemented."""
        pass
    
    def __repr__(self):
        """Provides a clean representation of the object during debugging."""
        return f"<{self.__class__.__name__} Object>"
