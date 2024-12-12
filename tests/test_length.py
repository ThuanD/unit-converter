import pytest
from converters.length import convert_length


def test_length_conversion():
    # Test meter to kilometer
    assert convert_length(1000, 'meter', 'kilometer') == pytest.approx(1.0)

    # Test inch to meter
    assert convert_length(39.3701, 'inch', 'meter') == pytest.approx(1.0)

    # Test mile to kilometer
    assert convert_length(1, 'mile', 'kilometer') == pytest.approx(1.6093)
