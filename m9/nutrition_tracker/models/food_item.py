class FoodItem:
    """
    A food item with nutrition info for one serving.

    Attributes:
        name: The name of the food.
        calories: Calories in one serving.
        protein: Protein (grams).
        carbs: Carbohydrates (grams).
        fat: Fat (grams).
        fiber: Fiber (grams).
        serving_size: What counts as one serving (ex: "1 cup", "100g").
    """
    def __init__(self, name, calories, protein, carbs, fat, fiber, serving_size):
        """
        Set up a food item with its nutrition info.
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.serving_size = serving_size

    def __str__(self):
        """
        Return a summary of the food.
        """
        return (
            f"{self.name} | {self.serving_size} | "
            f"{self.calories:.0f} cal | "
            f"Protein:{self.protein:.1f}g "
            f"Carbs:{self.carbs:.1f}g "
            f"Fat:{self.fat:.1f}g "
            f"Fiber:{self.fiber:.1f}g"
        )