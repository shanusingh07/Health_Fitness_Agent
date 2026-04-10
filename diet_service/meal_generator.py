def generate_meal_plan(user):
    goal = user.goal.lower()
    diet = user.diet.lower()

    meal_plan = {}

    # Basic logic based on goal
    if goal == "fat loss":
        meal_plan["breakfast"] = "Oats + Fruits"
        meal_plan["lunch"] = "Grilled vegetables + Dal"
        meal_plan["dinner"] = "Salad + Soup"
        meal_plan["snacks"] = "Nuts + Green tea"

    elif goal == "muscle gain":
        meal_plan["breakfast"] = "Milk + Banana + Peanut butter"
        meal_plan["lunch"] = "Rice + Dal + Paneer"
        meal_plan["dinner"] = "Roti + Paneer + Salad"
        meal_plan["snacks"] = "Protein shake / Nuts"

    else:  # maintenance
        meal_plan["breakfast"] = "Poha / Upma"
        meal_plan["lunch"] = "Roti + Sabzi + Dal"
        meal_plan["dinner"] = "Light dinner + Salad"
        meal_plan["snacks"] = "Fruits"

    # Adjust based on diet type
    if diet == "keto":
        meal_plan["breakfast"] = "Avocado + Eggs"
        meal_plan["lunch"] = "Paneer + Butter veggies"
        meal_plan["dinner"] = "Cheese salad"
        meal_plan["snacks"] = "Nuts"

    return meal_plan