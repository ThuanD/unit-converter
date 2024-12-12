def convert_weight(value, from_unit, to_unit):
    # Base conversion to kilograms
    to_kg_conversions = {
        "milligram": 0.000001,
        "gram": 0.001,
        "kilogram": 1,
        "ounce": 0.02834952,
        "pound": 0.45359237,
    }

    # Convert input to kilograms first
    kg = value * to_kg_conversions[from_unit]

    # Convert from kilograms to target unit
    result = kg / to_kg_conversions[to_unit]

    return round(result, 4)
