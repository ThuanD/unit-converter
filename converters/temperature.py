def convert_temperature(value, from_unit, to_unit):
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

    def celsius_to_kelvin(c):
        return c + 273.15

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5 / 9 + 273.15

    def kelvin_to_celsius(k):
        return k - 273.15

    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9 / 5 + 32

    # If same unit, return original value
    if from_unit == to_unit:
        return round(value, 4)

    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        value = fahrenheit_to_celsius(value)
    elif from_unit == "Kelvin":
        value = kelvin_to_celsius(value)

    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        result = celsius_to_fahrenheit(value)
    elif to_unit == "Kelvin":
        result = celsius_to_kelvin(value)
    else:
        result = value

    return round(result, 4)
