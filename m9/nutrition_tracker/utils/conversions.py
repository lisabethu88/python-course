def convert_to_grams(quantity, unit):
    """
    Converts a measurement into grams.
    """
    conversions = {
        "g": 1,
        "oz": 28.35,
        "lb": 453.6,
        "ml": 1,
        "fl oz": 29.57,
        "cup": 240,
        "tbsp": 15,
        "tsp": 5
    }

    return quantity * conversions.get(unit, 1)