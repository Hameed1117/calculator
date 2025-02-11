"""Calculator with DRY operations and history."""
from typing import Dict, Callable

class Calculation:
    """Handles arithmetic operations and stores history."""
    history: list = []
    _operations: Dict[str, Callable] = {}

    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

    # Map operation names to methods
    _operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    @classmethod
    def perform(cls, operation: str, a: float, b: float) -> float:
        """Perform a calculation using a DRY approach."""
        if operation not in cls._operations:
            raise ValueError(f"Invalid operation: {operation}")
        
        method = cls._operations[operation]
        result = method(a, b)
        cls.history.append(Calculation(operation, a, b, result))
        return result

    @classmethod
    def get_last(cls) -> "Calculation":
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history = []