# Services Package - Health Fitness Agent
# All services consolidated into single modules

from services.user_service import User, validate_user_data
from services.diet_service import generate_meal_plan, get_nutrition_tips
from services.fitness_service import generate_workout_plan, weekly_routine
from services.health_service import calculate_bmi, bmi_category, calculate_calories
from services.tracking_service import History, track_progress
