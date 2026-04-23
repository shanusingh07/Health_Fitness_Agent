# ============================================================
#                    MAIN.PY - ENTRY POINT
# ============================================================
# Ye file poore Health & Fitness Agent ka "starting point" hai.
# Jab tum "python main.py" run karte ho, sab kuch yahin se shuru hota hai.
#
# Ye file 4 kaam karti hai:
#   1. User se details leti hai (age, weight, height, goal, diet)
#   2. Health report banati hai (BMI, calories)
#   3. User ke sawaal samajhti hai (bmi/diet/workout)
#   4. Agar sawaal samajh nahi aaya → ChatGPT se jawaab leti hai
# ============================================================


# -------------------- STEP 0: IMPORTS --------------------
# Pehle hum zaroori cheezein import karte hain
# (Import = doosri files se code laana)

import sys   # System settings ke liye (jaise encoding fix karna)
import os    # Operating system se baat karne ke liye (jaise environment variables padhna)

# Terminal mein Hindi/emoji sahi dikhe, isliye encoding fix karte hain
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


# --- Apni services se zaroori functions/classes import kar rahe hain ---

# User Service: User ka data store + validate karne ke liye
from services.user_service import User, validate_user_data

# Diet Service: Khana ka plan banane ke liye
from services.diet_service import generate_meal_plan, get_nutrition_tips

# Fitness Service: Workout plan banane ke liye
from services.fitness_service import generate_workout_plan, weekly_routine

# Health Service: BMI calculate karna, category batana, calories nikalna
from services.health_service import calculate_bmi, bmi_category, calculate_calories

# Tracking Service: Progress track karna
from services.tracking_service import track_progress, History

# --- ChatGPT (OpenAI) se baat karne ke liye ---
from openai import OpenAI
from dotenv import load_dotenv  # .env file se secret keys padhne ke liye


# -------------------- STEP 1: CHATGPT SETUP --------------------
# .env file se OPENAI_API_KEY padhte hain
# (Ye key ChatGPT API use karne ke liye zaroori hai)

load_dotenv()  # .env file load karo

# OpenAI client banao, jisse hum ChatGPT ko request bhej sakein
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -------------------- STEP 2: AI FUNCTION --------------------
# Ye function ChatGPT ko sawaal bhejta hai aur jawaab laata hai
#
# Parameters:
#   query     = user ne kya pucha (jaise "how to lose belly fat?")
#   user_data = user ki details (age, weight, etc.)
#
# Return: ChatGPT ka jawaab (string mein)

def ask_ai(query, user_data):
    # ChatGPT ke liye ek prompt (instruction) banao
    prompt = f"""
    User details: {user_data}
    User query: {query}

    You are a fitness and health AI assistant.
    Give safe, practical and short advice.
    """

    # ChatGPT ko request bhejo
    response = client.chat.completions.create(
        model="gpt-5-mini",           # Konsa AI model use karna hai
        messages=[
            # System message = AI ko batao ki tum kaun ho
            {"role": "system", "content": "You are a helpful fitness and health assistant."},
            # User message = actual sawaal
            {"role": "user", "content": prompt}
        ],
        temperature=0.7  # 0 = strict jawaab, 1 = creative jawaab (0.7 = balanced)
    )

    # Response se sirf text nikalo aur return karo
    return response.choices[0].message.content


# -------------------- STEP 3: INTENT DETECTOR --------------------
# Ye class user ke sawaal mein se "intent" (iraada) samajhti hai
#
# Jaise:
#   "What is my bmi?"    → intent = "bmi"
#   "Give me a diet"     → intent = "diet"
#   "Suggest a workout"  → intent = "workout"
#   "How to sleep well?" → intent = "unknown" (ChatGPT handle karega)

class IntentDetector:

    def detect(self, query):
        # Sawaal ko chhote letters mein badlo taaki matching easy ho
        query = query.lower()

        # Keywords check karo
        if "bmi" in query:
            return "bmi"
        elif "diet" in query:
            return "diet"
        elif "workout" in query:
            return "workout"
        else:
            return "unknown"  # Koi bhi keyword match nahi hua


# -------------------- STEP 4: AGENT CONTROLLER --------------------
# Ye class poore agent ka "brain" hai
# Ye decide karti hai ki user ke sawaal ka jawaab kaise dena hai
#
# Kaam:
#   1. IntentDetector se intent pata karo
#   2. Intent ke hisaab se sahi service call karo
#   3. Agar intent samajh nahi aaya → ChatGPT se pucho

class AgentController:

    def __init__(self):
        # Intent Detector ka object banao
        self.detector = IntentDetector()

    def process(self, query, user_data):
        """
        User ke sawaal ko process karo aur jawaab do.

        Parameters:
            query     = user ka sawaal (string)
            user_data = user ki details (dictionary)

        Return: jawaab (string)
        """

        # Step A: Intent pata karo
        intent = self.detector.detect(query)

        # Step B: User data se User object banao
        user = User(**user_data)
        # **user_data matlab dictionary ke andar ki values ko
        # automatically User class mein daal do
        # Jaise: User(age=25, weight=70, height=170, goal="fat loss", diet="normal")

        # Step C: Intent ke hisaab se action lo

        if intent == "unknown":
            # Koi keyword match nahi hua → ChatGPT se jawaab lo
            print("🤖 Using ChatGPT to answer your question...")
            return ask_ai(query, user_data)

        elif intent == "bmi":
            # BMI calculate karo aur category batao
            bmi = calculate_bmi(user.weight, user.height)
            category = bmi_category(bmi)
            return f"BMI: {bmi:.2f}, Category: {category}"
            # {bmi:.2f} = BMI ko 2 decimal places tak dikhao

        elif intent == "diet":
            # Diet/Meal plan generate karo
            return generate_meal_plan(user)

        elif intent == "workout":
            # Workout plan generate karo
            return generate_workout_plan(user)


# -------------------- STEP 5: INPUT HELPERS --------------------
# Ye chhoti functions user se input lene mein madad karti hain
# Agar user galat value de → dubara puchti hain (loop mein)


def get_int_input(prompt):
    """User se ek integer (whole number) lo. Galat value pe dubara pucho."""
    while True:
        try:
            value = input(prompt).strip()  # .strip() = extra spaces hatao
            if not value:
                print("⚠️ Required field")  # Khali nahi chhod sakte
                continue  # Dubara pucho
            return int(value)  # String ko number mein badlo
        except:
            print("⚠️ Enter valid number")  # Galat input (jaise "abc")


def get_float_input(prompt):
    """User se ek decimal number lo. Galat value pe dubara pucho."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("⚠️ Required field")
                continue
            return float(value)  # String ko decimal number mein badlo
        except:
            print("⚠️ Enter valid number")


def get_choice_input(prompt, valid_options):
    """
    User se ek choice lo (jaise goal ya diet type).
    Sirf valid_options mein se hi accept karo.
    """
    while True:
        value = input(prompt).strip().lower()  # Lowercase mein convert karo
        if not value:
            print("⚠️ Required field")
            continue
        if value not in valid_options:
            # Agar user ne galat option diya
            print(f"⚠️ Choose from {valid_options}")
            continue
        return value


# -------------------- STEP 6: USER INPUT FUNCTION --------------------
# Ye function user se saari details ek saath leti hai
# Aur ek dictionary (key-value pairs) return karti hai

def get_user_input():
    print("\nEnter your details 👇\n")

    age = get_int_input("Age: ")
    weight = get_float_input("Weight (kg): ")
    height = get_float_input("Height (cm): ")

    goal = get_choice_input(
        "Goal (fat loss / muscle gain / maintenance): ",
        ["fat loss", "muscle gain", "maintenance"]
    )

    diet = get_choice_input(
        "Diet (vegetarian / keto / low carb / normal): ",
        ["vegetarian", "keto", "low carb", "normal"]
    )

    # Saari values ek dictionary mein return karo
    return {
        "age": age,
        "weight": weight,
        "height": height,
        "goal": goal,
        "diet": diet
    }


# ============================================================
#              STEP 7: MAIN FLOW (PROGRAM START)
# ============================================================
# Jab tum "python main.py" run karte ho, ye block chalta hai
# __name__ == "__main__" ka matlab hai: ye file directly run ho rahi hai
#   (kisi doosri file se import nahi ho rahi)

if __name__ == "__main__":

    # --- 7a. User se details lo ---
    data = get_user_input()

    # --- 7b. Data ko validate (check) karo ---
    # Kya age, weight, height sahi range mein hain?
    is_valid, message = validate_user_data(data)
    if not is_valid:
        print("❌ Error:", message)
        exit()  # Galat data hai → program band karo

    # --- 7c. User object banao ---
    user = User(**data)

    # --- 7d. Health Report generate karo ---
    bmi = calculate_bmi(user.weight, user.height)  # BMI nikalo
    category = bmi_category(bmi)                    # BMI category (underweight/normal/overweight)
    calories = calculate_calories(user)             # Daily calories nikalo

    # Health Report print karo
    print("\n===== 🏥 HEALTH REPORT =====")
    print(f"BMI: {bmi:.2f} | Category: {category}")
    print(f"Calories: {calories}")

    # --- 7e. BMI ke basis pe AI suggestion do ---
    print("\n🤖 AI SUGGESTION:")
    if bmi < 18.5:
        print("You are underweight → Focus on muscle gain")
    elif bmi <= 24.9:
        print("You are fit → Maintain balance")
    else:
        print("You are overweight → Focus on fat loss")

    # --- 7f. Agent (Chatbot) start karo ---
    controller = AgentController()

    print("\n🤖 Agent Ready! (type 'exit' to quit)")
    print("Try: bmi / diet / workout / any health question\n")

    # Infinite loop: jab tak user "exit" na type kare, sawaal puchte raho
    while True:
        query = input("👤 You: ")  # User se sawaal lo

        # Agar user ne "exit" likha → loop tod do, program band
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Agent se jawaab lo aur print karo
        response = controller.process(query, data)
        print("🤖 Agent:", response, "\n")