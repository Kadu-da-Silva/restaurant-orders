import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient


# Req3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        with open(source_path, newline='', encoding='utf-8') as csvfile:
            menu_reader = csv.DictReader(csvfile)

            for row in menu_reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None)

                if not dish:
                    dish = Dish(dish_name, dish_price)
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)

                # Add ingredient and recipe amount to the dish
                dish.add_ingredient_dependency(ingredient, recipe_amount)
