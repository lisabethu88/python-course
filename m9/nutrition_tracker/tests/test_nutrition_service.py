from unittest.mock import patch
from services.nutrition_service import get_food_item


@patch("services.nutrition_service.parse_nutrients")
@patch("services.nutrition_service.search_food")
def test_get_food_item_returns_none_for_fake_food(mock_search, mock_parse):

    # simulate "food not found"
    mock_search.return_value = None

    result = get_food_item("notrealfood123", 1, "g")

    assert result is None

@patch("services.nutrition_service.search_food")
@patch("services.nutrition_service.parse_nutrients")
def test_get_food_item_success(mock_parse, mock_search):

    mock_search.return_value = "fake_raw_data"

    mock_parse.return_value = {
        "calories": 100,
        "protein": 10,
        "carbs": 20,
        "fat": 5,
        "fiber": 2
    }

    result = get_food_item("apple", 100, "g")

    assert result.calories == 100
    assert result.protein == 10

@patch("services.nutrition_service.parse_nutrients")
@patch("services.nutrition_service.search_food")
@patch("services.nutrition_service.convert_to_grams")
def test_get_food_item_zero_grams(mock_convert, mock_search, mock_parse):

    mock_convert.return_value = 0

    result = get_food_item("apple", 1, "cup")

    assert result is None

@patch("services.nutrition_service.convert_to_grams")
def test_invalid_unit_returns_none(mock_convert):
    mock_convert.return_value = 0

    result = get_food_item("apple", 1, "invalid_unit")

    assert result is None

@patch("services.nutrition_service.parse_nutrients")
@patch("services.nutrition_service.search_food")
@patch("services.nutrition_service.convert_to_grams")
def test_nutrient_scaling(mock_convert, mock_search, mock_parse):

    mock_convert.return_value = 200  # scale = 2
    mock_search.return_value = "fake_data"

    mock_parse.return_value = {
        "calories": 50,
        "protein": 10,
        "carbs": 0,
        "fat": 0,
        "fiber": 0
    }

    result = get_food_item("apple", 2, "cup")

    assert result.calories == 100
    assert result.protein == 20

@patch("services.nutrition_service.parse_nutrients")
@patch("services.nutrition_service.search_food")
@patch("services.nutrition_service.convert_to_grams")
def test_serving_size_saved(mock_convert, mock_search, mock_parse):

    mock_convert.return_value = 100
    mock_search.return_value = "fake_data"

    mock_parse.return_value = {
        "calories": 100,
        "protein": 10,
        "carbs": 10,
        "fat": 10,
        "fiber": 10
    }

    result = get_food_item("banana", 1.5, "cup")

    assert result.serving_size == "1.5 cup"