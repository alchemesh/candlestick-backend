import pytest
from Stock import Stock

@pytest.fixture(scope="class")
def stock_class_instance():
    """A pytest fixture that provides an instance of MyClass."""
    return Stock({
        "eventID": "TEST",
        "ticker": "MSFT",
        "timestamp": "Future Time"
      }, "Microsoft")

@pytest.mark.usefixtures("stock_class_instance")
class TestStock:
    def test_stock_name(self, stock_class_instance):
        assert stock_class_instance.getName() == "Microsoft"

    def test_stock_event(self, stock_class_instance):
        expected_data = { "eventID": "TEST", "ticker": "MSFT", "timestamp": "Future Time" }
        assert stock_class_instance.getEvent() == expected_data
