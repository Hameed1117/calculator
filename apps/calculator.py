"""Intermediate calculator with DRY operations and parameterized testing."""
from typing import Dict, Callable, Optional, List

class Calculation:
    """Handles arithmetic operations and stores history."""
    history: List["Calculation"] = []
    _operations: Dict[str, Callable[[float, float], float]] = {}

    def __init__(self, operation: str, num1: float, num2: float, result: float) -> None:
        """Initialize a new calculation."""
        self.operation = operation
        self.num1 = num1
        self.num2 = num2
        self.result = result

    @staticmethod
    def add(num1: float, num2: float) -> float:
        """Add two numbers."""
        return num1 + num2

    @staticmethod
    def subtract(num1: float, num2: float) -> float:
        """Subtract second number from first."""
        return num1 - num2

    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        """Multiply two numbers."""
        return num1 * num2

    @staticmethod
    def divide(num1: float, num2: float) -> float:
        """Divide first number by second."""
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return num1 / num2

    # Initialize operations map after methods are defined
    _operations.update({
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    })

    @classmethod
    def perform(cls, operation: str, num1: float, num2: float) -> float:
        """Perform a calculation using a DRY approach."""
        if operation not in cls._operations:
            raise ValueError(f"Invalid operation: {operation}")
        method = cls._operations[operation]
        result = method(num1, num2)
        cls.history.append(Calculation(operation, num1, num2, result))
        return result

    @classmethod
    def get_last(cls) -> Optional["Calculation"]:
        """Return the last calculation or None if history is empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history."""
        cls.history = []
