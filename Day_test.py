import pytest
from Day import Day

@pytest.fixture(scope="class")
def day_class_instance():
    """A pytest fixture that provides an instance of MyClass."""
    return Day("Future Time", 255.48, 262.07, 263.08, 254.23)

@pytest.mark.usefixtures("day_class_instance")
class TestDay:
    def test_day_high(self, day_class_instance):
        assert day_class_instance.getHigh() == 263.08

    def test_day_low(self, day_class_instance):
        assert day_class_instance.getLow() == 254.23

    def test_day_getstate(self, day_class_instance):
        day_class_instance.updateState()
        assert day_class_instance.getState() == "Bullish"