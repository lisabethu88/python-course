from .api import parse_nutrients, search_food
from utils.conversions import convert_to_grams
from models.food_item import FoodItem

def get_food_item(food_name, quantity, unit):
    """Gets a food item with nutrition info based on a given amount.

    Converts the input amount to grams, looks up the food in the API,
    pulls its nutrients, and scales the values based on the amount.

    Args:
        food_name: Name of the food to search for.
        quantity: How much of the food (ex: 2, 1.5).
        unit: Unit of measurement (ex: "cup", "g", "tbsp").

    Returns:
        A FoodItem object with nutrition values for the amount the user entered
        or None if the food is not found.
    """
    grams = convert_to_grams(quantity, unit)

    if grams == 0:
        return None

    raw_data = search_food(food_name)
    if not raw_data:
        print("Food not found")
        return None

    nutrients = parse_nutrients(raw_data)

    scale = grams / 100  # adjust values based on how much food was entered
    
    return FoodItem(
        name=food_name,
        calories=nutrients["calories"] * scale,
        protein=nutrients["protein"] * scale,
        fiber=nutrients["fiber"] * scale,
        carbs=nutrients["carbs"] * scale,
        fat=nutrients["fat"] * scale,
        serving_size=f"{quantity} {unit}"
    )   