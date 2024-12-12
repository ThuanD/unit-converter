import pytest
from converters.temperature import convert_temperature


def test_temperature_conversion():
    # Test Celsius to Fahrenheit
    assert convert_temperature(0, 'Celsius', 'Fahrenheit') == pytest.approx(32.0)

    # Test Fahrenheit to Kelvin
    assert convert_temperature(32, 'Fahrenheit', 'Kelvin') == pytest.approx(273.15)

    # Test Kelvin to Celsius
    assert convert_temperature(273.15, 'Kelvin', 'Celsius') == pytest.approx(0.0)
