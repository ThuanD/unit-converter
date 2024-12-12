def convert_length(value, from_unit, to_unit):
    # Base conversion to meters
    to_meter_conversions = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
    }

    # Convert input to meters first
    meters = value * to_meter_conversions[from_unit]

    # Convert from meters to target unit
    result = meters / to_meter_conversions[to_unit]

    return round(result, 4)
