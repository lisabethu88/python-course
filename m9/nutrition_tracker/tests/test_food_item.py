from models.food_item import FoodItem

def test_food_item_stores_values():
    item = FoodItem(
        name="apple",
        calories=100,
        protein=10,
        carbs=20,
        fat=5,
        fiber=2,
        serving_size="1 cup"
    )

    assert item.name == "apple"
    assert item.calories == 100
    assert item.protein == 10
    assert item.carbs == 20
    assert item.fat == 5
    assert item.fiber == 2
    assert item.serving_size == "1 cup"

from models.food_item import FoodItem


def test_food_item_str():
    item = FoodItem(
        name="apple",
        calories=95.7,
        protein=0.3,
        carbs=25.4,
        fat=0.2,
        fiber=4.1,
        serving_size="1 medium"
    )

    result = str(item)

    expected = (
        "apple | 1 medium | "
        "96 cal | "
        "Protein:0.3g "
        "Carbs:25.4g "
        "Fat:0.2g "
        "Fiber:4.1g"
    )

    assert result == expected