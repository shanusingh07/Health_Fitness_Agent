def calculate_calories(user):
    """
    Estimate daily calorie needs using the Mifflin-St Jeor equation.
    Assumes moderate activity level and adjusts based on goal.
    """
    # Base BMR (using male formula as default since gender isn't in User)
    bmr = 10 * user.weight + 6.25 * user.height - 5 * user.age + 5

    # Moderate activity multiplier
    maintenance = bmr * 1.55

    goal = user.goal.lower()
    if goal == "fat loss":
        return round(maintenance - 500)
    elif goal == "muscle gain":
        return round(maintenance + 300)
    else:
        return round(maintenance)