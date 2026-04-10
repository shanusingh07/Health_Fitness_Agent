def get_nutrition_tips(user):
    weight = user.weight

    # Simple logic
    water_intake = round(weight * 0.04, 2)  # liters
    fiber = "25-35g per day"

    tips = {
        "hydration": f"{water_intake}L water/day",
        "fiber": fiber,
        "electrolytes": "Include sodium, potassium, magnesium"
    }

    return tips