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