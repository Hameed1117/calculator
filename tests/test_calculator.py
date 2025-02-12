"""Advanced tests for calculator with type validation."""
import pytest
from apps.calculator import Calculation, HistoryManager

@pytest.fixture(autouse=True)
def clear_history():
    """Clear the history before each test."""
    HistoryManager.clear()
    yield

def test_type_validation():
    """Test that type validation works."""
    with pytest.raises(TypeError):
        Calculation.add("2", 3)  # Invalid type

def test_basic_operations():
    """Test all basic arithmetic operations."""
    assert Calculation.perform("add", 2, 3) == 5
    assert Calculation.perform("subtract", 5, 3) == 2
    assert Calculation.perform("multiply", 4, 3) == 12
    assert Calculation.perform("divide", 6, 2) == 3

def test_division_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ZeroDivisionError):
        Calculation.perform("divide", 5, 0)

def test_invalid_operation():
    """Test invalid operation raises error."""
    with pytest.raises(ValueError):
        Calculation.perform("invalid_op", 2, 3)

def test_history_manager():
    """Test that history manager stores calculations correctly."""
    Calculation.perform("add", 2, 3)
    last_calc = HistoryManager.get_last()
    assert last_calc is not None
    assert last_calc.result == 5
    assert last_calc.operation == "add"
    assert last_calc.a == 2
    assert last_calc.b == 3

def test_multiple_calculations():
    """Test multiple calculations are stored correctly."""
    Calculation.perform("add", 2, 3)
    Calculation.perform("multiply", 4, 5)
    last_calc = HistoryManager.get_last()
    assert last_calc.result == 20
    assert last_calc.operation == "multiply"

def test_history_clear():
    """Test history clearing functionality."""
    Calculation.perform("add", 2, 3)
    Calculation.clear_history()
    assert HistoryManager.get_last() is None
