from utils.conversions import convert_to_grams

def test_convert_oz_to_grams():
    assert convert_to_grams(1, "oz") == 28.35

def test_convert_lb_to_grams():
    assert convert_to_grams(1, "lb") == 453.6

def test_convert_unknown_unit():
    assert convert_to_grams(10, "unknown") == 10

# edge case
def test_convert_to_grams_unknown_unit():
    assert convert_to_grams(5, "banana") == 5