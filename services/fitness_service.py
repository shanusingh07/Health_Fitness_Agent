def generate_workout_plan(user):
    goal = user.goal.lower()

    workout_plan = {}

    if goal == "fat loss":
        workout_plan["warmup"] = "Jump rope - 5 min"
        workout_plan["main_workout"] = [
            "Running - 20 min",
            "Burpees - 3 sets x 12 reps",
            "Mountain climbers - 3 sets x 20 reps"
        ]
        workout_plan["cooldown"] = "Stretching - 5 min"

    elif goal == "muscle gain":
        workout_plan["warmup"] = "Light jogging - 5 min"
        workout_plan["main_workout"] = [
            "Push-ups - 4 sets x 10 reps",
            "Squats - 4 sets x 12 reps",
            "Dumbbell curls - 3 sets x 10 reps"
        ]
        workout_plan["cooldown"] = "Stretching - 5 min"

    else:  # maintenance
        workout_plan["warmup"] = "Walking - 5 min"
        workout_plan["main_workout"] = [
            "Light jogging - 15 min",
            "Bodyweight exercises - 3 sets"
        ]
        workout_plan["cooldown"] = "Stretching - 5 min"

    return workout_plan


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
