# User Service
from user_services.user import User
from user_services.validation import validate_user_data

# Diet Service
from diet_service.meal_generator import generate_meal_plan
from diet_service.nutrition import get_nutrition_tips

# Fitness Service
from fitness_service.workout_generator import generate_workout_plan
from fitness_service.routine import weekly_routine

# Health Service
from health_service.bmi import calculate_bmi, bmi_category
from health_service.calorie import calculate_calories

# Tracking Service
from tracking_service.progress import track_progress
from tracking_service.history import History




class IntentDetector:
    def detect(self, query):
        query = query.lower()

        if "bmi" in query:
            return "bmi"

        elif "diet" in query:
            return "diet"

        elif "workout" in query:
            return "workout"

        else:
            return "unknown"


# 🔥 Helper functions for safe input
def get_int_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("⚠️  This field is required. Please enter a value.")
                continue
            return int(value)
        except ValueError:
            print("⚠️  Please enter a valid whole number.")


def get_float_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("⚠️  This field is required. Please enter a value.")
                continue
            return float(value)
        except ValueError:
            print("⚠️  Please enter a valid number.")


def get_choice_input(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if not value:
            print("⚠️  This field is required. Please enter a value.")
            continue
        if value not in valid_options:
            print(f"⚠️  Please choose from: {' / '.join(valid_options)}")
            continue
        return value


# 🔥 User input function
def get_user_input():
    print("\nEnter your details 👇\n")

    age = get_int_input("Age: ")
    weight = get_float_input("Weight (kg): ")
    height = get_float_input("Height (cm): ")
    goal = get_choice_input("Goal (fat loss / muscle gain / maintenance): ",
                            ["fat loss", "muscle gain", "maintenance"])
    diet = get_choice_input("Diet (vegetarian / keto / low carb / normal): ",
                            ["vegetarian", "keto", "low carb", "normal"])

    return {
        "age": age,
        "weight": weight,
        "height": height,
        "goal": goal,
        "diet": diet
    }


def main():
    # 🔹 Step 1: Take user input (UPDATED)
    data = get_user_input()

    # 🔹 Step 2: Validate Data
    is_valid, message = validate_user_data(data)

    if not is_valid:
        print("Error:", message)
        return

    # 🔹 Step 3: Create User Object
    user = User(**data)

    # 🔹 Step 4: Health Calculations
    bmi = calculate_bmi(user.weight, user.height)
    category = bmi_category(bmi)
    calories = calculate_calories(user)

    # 🔹 Step 5: Diet Plan
    diet_plan = generate_meal_plan(user)
    nutrition = get_nutrition_tips(user)

    # 🔹 Step 6: Fitness Plan
    workout = generate_workout_plan(user)
    routine = weekly_routine(user.goal)

    # 🔹 Step 7: Tracking
    history = History()
    history.add_record({"weight": user.weight})
    history.add_record({"weight": user.weight - 2})

    progress = track_progress(user, user.weight - 2, user.weight)

    # 🔥 Final Output
    print("\n===== HEALTH REPORT =====")
    print("BMI:", bmi, "| Category:", category)
    print("Daily Calories:", calories)

    print("\n===== DIET PLAN =====")
    print(diet_plan)
    print("Nutrition Tips:", nutrition)

    print("\n===== FITNESS PLAN =====")
    print(workout)
    print("Weekly Routine:", routine)

    print("\n===== PROGRESS =====")
    print(progress)
    print("History:", history.get_history())


# Run app
if __name__ == "__main__":
    main()