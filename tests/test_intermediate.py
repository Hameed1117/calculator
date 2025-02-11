"""Intermediate tests with parameterization."""
import pytest
from apps.calculator import Calculation

@pytest.mark.parametrize(
    "operation, num1, num2, expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 10, 4, 6),
        ("multiply", 3, 5, 15),
        ("divide", 20, 4, 5),
    ],
)
def test_operations(operation: str, num1: float, num2: float, expected: float) -> None:
    """Test basic arithmetic operations with parameterized inputs."""
    assert Calculation.perform(operation, num1, num2) == expected
    assert Calculation.get_last().result == expected

def test_invalid_operation() -> None:
    """Test that invalid operations raise ValueError."""
    with pytest.raises(ValueError):
        Calculation.perform("invalid", 2, 3)
