import pytest
from Stock import Stock

@pytest.fixture
def stock_class_instance():
    """A pytest fixture that provides an instance of MyClass."""
    return Stock({
        "eventID": "TEST",
        "ticker": "MSFT",
        "timestamp": "Future Time"
      }, "Microsoft")

class TestStock:
    def test_add(self):
        assert stock_class_instance.getName() == "Microsoft"
