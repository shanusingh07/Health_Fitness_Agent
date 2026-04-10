def weekly_routine(goal):
    goal = goal.lower()

    if goal == "fat loss":
        return {
            "Monday": "Cardio",
            "Tuesday": "HIIT",
            "Wednesday": "Rest",
            "Thursday": "Cardio",
            "Friday": "Strength + Cardio",
            "Saturday": "HIIT",
            "Sunday": "Rest"
        }

    elif goal == "muscle gain":
        return {
            "Monday": "Chest + Triceps",
            "Tuesday": "Back + Biceps",
            "Wednesday": "Legs",
            "Thursday": "Shoulders",
            "Friday": "Full Body",
            "Saturday": "Light Cardio",
            "Sunday": "Rest"
        }

    else:
        return {
            "Monday": "Light Workout",
            "Tuesday": "Cardio",
            "Wednesday": "Rest",
            "Thursday": "Strength",
            "Friday": "Cardio",
            "Saturday": "Yoga",
            "Sunday": "Rest"
        }