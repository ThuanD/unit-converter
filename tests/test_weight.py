import pytest
from converters.weight import convert_weight


def test_weight_conversion():
    # Test kilogram to pound
    assert convert_weight(1, 'kilogram', 'pound') == pytest.approx(2.2046)

    # Test gram to kilogram
    assert convert_weight(1000, 'gram', 'kilogram') == pytest.approx(1.0)

    # Test ounce to gram
    assert convert_weight(1, 'ounce', 'gram') == pytest.approx(28.3495)
