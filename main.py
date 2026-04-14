import sys
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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

# 🔥 ChatGPT Setup
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔥 AI function
def ask_ai(query, user_data):
    prompt = f"""
    User details: {user_data}
    User query: {query}

    You are a fitness and health AI assistant.
    Give safe, practical and short advice.
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are a helpful fitness and health assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# 🔥 Intent Detector
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


# 🔥 Agent Controller
class AgentController:

    def __init__(self):
        self.detector = IntentDetector()

    def process(self, query, user_data):
        intent = self.detector.detect(query)
        user = User(**user_data)

        # 🔥 AI fallback
        if intent == "unknown":
            print("🤖 Using ChatGPT to answer your question...")
            return ask_ai(query, user_data)

        if intent == "bmi":
            bmi = calculate_bmi(user.weight, user.height)
            category = bmi_category(bmi)
            return f"BMI: {bmi:.2f}, Category: {category}"

        elif intent == "diet":
            return generate_meal_plan(user)

        elif intent == "workout":
            return generate_workout_plan(user)


# 🔥 Input helpers
def get_int_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("⚠️ Required field")
                continue
            return int(value)
        except:
            print("⚠️ Enter valid number")


def get_float_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("⚠️ Required field")
                continue
            return float(value)
        except:
            print("⚠️ Enter valid number")


def get_choice_input(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if not value:
            print("⚠️ Required field")
            continue
        if value not in valid_options:
            print(f"⚠️ Choose from {valid_options}")
            continue
        return value


# 🔥 User input
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


# 🔥 MAIN FLOW
if __name__ == "__main__":

    # Step 1: Input
    data = get_user_input()

    # Step 2: Validate
    is_valid, message = validate_user_data(data)
    if not is_valid:
        print("❌ Error:", message)
        exit()

    user = User(**data)

    # Step 3: Health Report
    bmi = calculate_bmi(user.weight, user.height)
    category = bmi_category(bmi)
    calories = calculate_calories(user)

    print("\n===== 🏥 HEALTH REPORT =====")
    print(f"BMI: {bmi:.2f} | Category: {category}")
    print(f"Calories: {calories}")

    # 🔥 AI Suggestion
    print("\n🤖 AI SUGGESTION:")
    if bmi < 18.5:
        print("You are underweight → Focus on muscle gain")
    elif bmi <= 24.9:
        print("You are fit → Maintain balance")
    else:
        print("You are overweight → Focus on fat loss")

    # Step 4: Agent Start
    controller = AgentController()

    print("\n🤖 Agent Ready! (type 'exit' to quit)")
    print("Try: bmi / diet / workout / any health question\n")

    while True:
        query = input("👤 You: ")

        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        response = controller.process(query, data)
        print("🤖 Agent:", response, "\n")