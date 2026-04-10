def validate_user_data(data):
    required_fields = ["age", "weight", "height", "goal", "diet"]

    # Check missing fields
    for field in required_fields:
        if field not in data:
            return False, f"{field} is required"

    # Validate age
    if not isinstance(data["age"], int) or data["age"] <= 0:
        return False, "Age must be a positive integer"

    # Validate weight
    if not isinstance(data["weight"], (int, float)) or data["weight"] <= 0:
        return False, "Weight must be a positive number"

    # Validate height
    if not isinstance(data["height"], (int, float)) or data["height"] <= 0:
        return False, "Height must be a positive number"

    # Validate goal
    valid_goals = ["fat loss", "muscle gain", "maintenance"]
    if data["goal"].lower() not in valid_goals:
        return False, f"Goal must be one of {valid_goals}"

    # Validate diet
    valid_diets = ["vegetarian", "keto", "low carb", "normal"]
    if data["diet"].lower() not in valid_diets:
        return False, f"Diet must be one of {valid_diets}"

    return True, "Valid data"