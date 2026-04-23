# 🏋️ Health Fitness Agent

## 📌 Overview

Health Fitness Agent is a Python-based modular application designed using a microservice-style architecture.
It provides personalized responses for user queries related to:

* BMI calculation
* Diet plans
* Workout routines
* General health tips

The system simulates a basic AI agent by combining multiple services with an intent detection and controller layer.

---

## ⚙️ Features

* 🔹 BMI calculation with category classification
* 🔹 Personalized diet plan generation
* 🔹 Workout plan suggestions
* 🔹 Health and nutrition tips
* 🔹 Interactive command-line chatbot
* 🔹 Input validation (safe user inputs)
* 🔹 Modular and scalable architecture

---

## 🧠 Architecture

The project follows a layered architecture:

```
User Input
    ↓
Chat Interface (main.py)
    ↓
Agent Controller
    ↓
Intent Detector
    ↓
Service Layer (Diet / Fitness / Health)
    ↓
Response to User
```

---

## 📂 Project Structure

```
Health_Fitness_agent/
│
├── main.py                  # Entry point (chat interface)
│
├── services/                # All microservices in one folder
│   ├── __init__.py          # Package exports
│   ├── diet_service.py      # Meal plans + nutrition tips
│   ├── fitness_service.py   # Workout plans + weekly routine
│   ├── health_service.py    # BMI + calorie calculation
│   ├── tracking_service.py  # History + progress tracking
│   └── user_service.py      # User model + validation
│
├── frontend/                # Web UI
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
├── SETUP.md                 # Setup instructions
├── ISSUES.md                # Known issues
├── RESEARCH.md              # Technical research
├── Progress.md              # Daily progress log
└── README.md
```

---

## 🔍 Core Components

### 1. Intent Detector

* Identifies user intent based on keywords
* Example:

  * "bmi" → BMI calculation
  * "diet" → Meal plan
  * "workout" → Fitness routine

---

### 2. Agent Controller

* Acts as the brain of the system
* Routes user queries to the correct service
* Combines intent detection with business logic

---

### 3. Services Layer

#### 🥗 Diet Service

* Generates meal plans
* Provides nutrition tips

#### 💪 Fitness Service

* Generates workout routines
* Weekly exercise planning

#### ❤️ Health Service

* BMI calculation
* Health-related metrics

---

### 4. Input Handling

Custom helper functions ensure:

* No empty input
* Valid numeric values
* Controlled user interaction

---

## 🚀 How It Works

1. User enters a query (e.g., "calculate my BMI")
2. Intent Detector analyzes the query
3. Controller selects the correct service
4. Service processes data
5. Response is returned to the user

---

## ▶️ How to Run

```bash
python main.py
```

---

## 💬 Example Usage

```
You: bmi bata
Agent: Your BMI is 22.5 (Normal)

You: diet plan do
Agent: [Generated Meal Plan]

You: workout bata
Agent: [Workout Routine]
```

---

## 🛠️ Technologies Used

* Python
* Modular programming
* CLI-based interaction

---

## 🔮 Future Improvements

* Integration with AI models (OpenAI / Gemini)
* GUI interface (PyQt / Web App)
* User history tracking
* Voice-based interaction
* Advanced NLP for better understanding

---

## 📌 Conclusion

This project demonstrates how a simple rule-based system can simulate an AI agent by combining:

* Intent detection
* Controller logic
* Modular services

It is a strong foundation for building advanced AI-powered assistants.

---
