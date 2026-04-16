from ui.app import FoodTrackerApp
from unittest.mock import patch
import tkinter as tk
from models.food_item import FoodItem

def test_update_totals_dict():
    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "fiber": 0
    }

    item = FoodItem("apple", 100, 10, 20, 5, 2, "1 cup")

    result = FoodTrackerApp.update_totals_dict(totals, item)

    assert result["calories"] == 100
    assert result["protein"] == 10
    assert result["carbs"] == 20
    assert result["fat"] == 5
    assert result["fiber"] == 2


def test_add_food_empty_input():
    root = tk.Tk()
    app = FoodTrackerApp(root)

    app.food_name_entry.insert(0, "")
    app.quantity_entry.insert(0, "1")

    app.add_food()

    assert len(app.log_listbox.get(0, tk.END)) == 0


def test_add_food_invalid_quantity():
    root = tk.Tk()
    app = FoodTrackerApp(root)

    app.food_name_entry.insert(0, "apple")
    app.quantity_entry.insert(0, "abc")  # invalid
    app.unit_combobox.set("g")

    app.add_food()

    assert len(app.log_listbox.get(0, tk.END)) == 0


@patch("ui.app.get_food_item")
def test_add_food_success(mock_get_food):
    root = tk.Tk()
    app = FoodTrackerApp(root)

    mock_get_food.return_value = FoodItem(
        "apple", 100, 10, 20, 5, 2, "1 cup"
    )

    app.food_name_entry.insert(0, "apple")
    app.quantity_entry.insert(0, "1")
    app.unit_combobox.set("g")

    app.add_food()

    # list updated
    assert len(app.log_listbox.get(0, tk.END)) == 1

    # totals updated
    assert app.totals["calories"] == 100
    assert app.totals["protein"] == 10