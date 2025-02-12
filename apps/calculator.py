"""Advanced calculator with type validation and a history manager."""
from typing import List, Optional
from functools import wraps

class HistoryManager:
    """Manages calculation history."""
    _history: List["Calculation"] = []

    @classmethod
    def add_entry(cls, calculation: "Calculation"):
        """Add a calculation to history."""
        cls._history.append(calculation)

    @classmethod
    def get_last(cls) -> Optional["Calculation"]:
        """Get the most recent calculation."""
        return cls._history[-1] if cls._history else None

    @classmethod
    def clear(cls):
        """Clear all history."""
        cls._history = []

def validate_input(func):
    """Decorator to validate input types."""
    @wraps(func)
    def wrapper(a: float, b: float) -> float:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Operands must be numbers")
        return func(a, b)
    return wrapper

class Calculation:
    """Handles arithmetic operations with validation."""
    
    def __init__(self, operation: str, a: float, b: float, result: float):
        """Initialize a calculation instance."""
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    @staticmethod
    @validate_input
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @staticmethod
    @validate_input
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b

    @staticmethod
    @validate_input
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    @validate_input
    def divide(a: float, b: float) -> float:
        """Divide two numbers."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @classmethod
    def perform(cls, operation: str, a: float, b: float) -> float:
        """Perform a calculation and store it in history."""
        method = getattr(cls, operation, None)
        if not method:
            raise ValueError(f"Invalid operation: {operation}")
        
        result = method(a, b)
        entry = cls(operation, a, b, result)
        HistoryManager.add_entry(entry)
        return result

    @classmethod
    def get_last(cls) -> Optional["Calculation"]:
        """Get the most recent calculation."""
        return HistoryManager.get_last()

    @classmethod
    def clear_history(cls):
        """Clear all calculation history."""
        HistoryManager.clear()