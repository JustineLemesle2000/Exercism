"""Functions for compiling dishes and ingredients for a catering company."""
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
   return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    for item in drink_ingredients :
        if item in ALCOHOLS : 
            return drink_name + " Cocktail"
    return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    categories = [
        (VEGAN, "VEGAN"),
        (VEGETARIAN, "VEGETARIAN"),
        (PALEO, "PALEO"),
        (KETO, "KETO"),
        (OMNIVORE, "OMNIVORE")
    ]     
    for category_set, category_name in categories :
        if dish_ingredients.issubset(category_set) :
            return f"{dish_name}: {category_name}"
    return f"{dish_name}: UNKNOWN"


def tag_special_ingredients(dish):
    special_ingredient = SPECIAL_INGREDIENTS.intersection(dish[1])
    return (dish[0], special_ingredient)


def compile_ingredients(dishes):
    result = set()
    for dish in dishes : 
        result = result.union(dish)
    return result

def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))

def singleton_ingredients(dishes, intersection):
    result = set()
    for dish in dishes: 
        result = result.union(dish)
    return result - intersection
    
        
