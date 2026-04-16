import requests
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("USDA_API_KEY")
BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"


def search_food(food_name):
    """Search for a food by name using the usda.gov API and return the first result.

        Args:
            food_name: The name of the food to look up.

        Returns:
            A dictionary with food data if its found or None if no results are found.

        Raises:
            HTTPError: If the API request fails.
    """

    params = {
        "api_key": API_KEY,
        "query": food_name,
        "pageSize": 1
    }

    response = requests.get(BASE_URL, params=params) # make a request
    response.raise_for_status() # raises HTTPerror

    data = response.json()

    if not data.get("foods"):
        return None

    return data["foods"][0] # return the first food result from the list

def parse_nutrients(food_data):
    """Extracts nutrition values from raw food data.

    Takes the nutrient list from the API response and pulls out
    calories, protein, fiber, fat, and carbs.

    Args:
        food_data: A dictionary containing food information from the API.

    Returns:
        A dictionary with these nutrient values:
        - calories
        - protein
        - fiber
        - fat
        - carbs
    """

    nutrients = food_data.get("foodNutrients", [])

    result = {
        "calories": 0,
        "protein": 0,
        "fiber": 0,
        "fat": 0,
        "carbs": 0
    }

    for nutrient in nutrients:
        name = nutrient.get("nutrientName", "").lower()
        value = nutrient.get("value", 0)

        if "energy" in name:  
            result["calories"] = value
        elif "protein" in name:
            result["protein"] = value
        elif "fiber" in name:
            result["fiber"] = value
        elif "total lipid (fat)" in name:
            result["fat"] = value
        elif "carbohydrate" in name:
            result["carbs"] = value

    return result