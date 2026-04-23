# Health & Fitness Agent

Health & Fitness Agent is a small modular Python project that collects a user's fitness profile, generates a basic health report, and responds to health-related queries through dedicated service modules. The repository also includes a separate frontend prototype that demonstrates how the experience could look in a browser.

The project is best understood as a layered agent system:

- Profile input and validation
- Health calculations
- Intent detection and request routing
- Domain services for diet and fitness
- OpenAI fallback for general health questions

## What The Project Does

- Collects age, weight, height, goal, and diet preference
- Validates the user profile before processing
- Calculates BMI and calorie targets
- Generates simple meal plans
- Generates simple workout plans
- Supports progress tracking utilities
- Falls back to OpenAI for questions outside the keyword-based intents

## Architecture Overview

The runtime flow in `main.py` looks like this:

```text
User
  |
  v
CLI Input Helpers
  |
  v
User Profile Dictionary
  |
  v
validate_user_data()
  |
  v
User Object
  |
  +------------------------------+
  |                              |
  v                              v
Health Report                AgentController
(BMI + calories)                 |
                                 v
                         IntentDetector.detect()
                                 |
                +----------------+----------------+
                |                |                |
                v                v                v
              "bmi"            "diet"         "workout"
                |                |                |
                v                v                v
         health_service    diet_service     fitness_service
                |
                v
            otherwise
                |
                v
         OpenAI fallback via ask_ai()
```

## Project Structure

```text
Health_Fitness_agent/
|-- main.py
|-- README.md
|-- SETUP.md
|-- ISSUES.md
|-- RESEARCH.md
|-- Progress.md
|-- requirements.txt
|-- .env
|-- .env.example
|-- frontend/
|   |-- index.html
|   |-- style.css
|   `-- app.js
`-- services/
    |-- __init__.py
    |-- user_service.py
    |-- health_service.py
    |-- diet_service.py
    |-- fitness_service.py
    `-- tracking_service.py
```

## Folder And File Responsibilities

### `main.py`

This is the entry point and coordinator of the backend flow.

- Loads environment variables
- Creates the OpenAI client
- Collects and validates user input
- Builds the initial health report
- Runs the chatbot loop
- Routes each user query through the controller

### `services/`

This folder contains the application logic split by responsibility.

#### `services/user_service.py`

- Defines the `User` model
- Converts user data into dictionary form
- Validates input fields and allowed values

#### `services/health_service.py`

- Calculates BMI
- Maps BMI to a category
- Estimates daily calorie targets based on goal

#### `services/diet_service.py`

- Creates a simple meal plan from goal and diet type
- Generates nutrition tips such as hydration guidance

#### `services/fitness_service.py`

- Creates workout plans based on the user's goal
- Provides a weekly routine helper

#### `services/tracking_service.py`

- Stores simple history records
- Compares current and previous weight to track progress

#### `services/__init__.py`

- Re-exports service functions and classes
- Makes imports simpler for package-level use

### `frontend/`

This is a standalone UI prototype, not a fully integrated frontend.

#### `frontend/index.html`

- Defines the onboarding form
- Defines the dashboard/chat layout
- Shows the health summary panel and chat area

#### `frontend/style.css`

- Implements the visual design
- Handles layout, form styling, chat styling, and animations

#### `frontend/app.js`

- Manages frontend interactions
- Simulates profile submission and health report generation
- Simulates chat replies in the browser
- Currently uses mock logic instead of calling the Python backend

### Project Documentation Files

- `SETUP.md`: installation and setup guidance
- `ISSUES.md`: known issues and pending gaps
- `RESEARCH.md`: research notes and reference thinking
- `Progress.md`: progress tracking and development notes

## Component-Level Design

### 1. Input Layer

The input helper functions in `main.py` make sure the CLI experience stays controlled.

- `get_int_input()`
- `get_float_input()`
- `get_choice_input()`
- `get_user_input()`

These functions reduce invalid input before the data reaches the service layer.

### 2. Validation Layer

`validate_user_data()` in `services/user_service.py` ensures:

- Required fields exist
- Numeric values are positive
- Goal is one of the allowed options
- Diet is one of the allowed options

### 3. Domain Model

The `User` class acts as the shared data model passed into services.

```text
User
|-- age
|-- weight
|-- height
|-- goal
`-- diet
```

### 4. Health Analysis Layer

The project produces an initial report before chat begins.

- `calculate_bmi(weight, height)`
- `bmi_category(bmi)`
- `calculate_calories(user)`

This gives the user a quick summary of their current condition and target calories.

### 5. Intent Detection Layer

`IntentDetector` is keyword-based and currently recognizes:

- `bmi`
- `diet`
- `workout`
- `unknown`

Any query outside those keywords goes to the AI fallback path.

### 6. Agent Controller Layer

`AgentController` is the central router.

- Detects the intent
- Creates the `User` object
- Calls the correct service
- Uses OpenAI if the intent is unknown

This is the closest thing to the system's orchestration layer.

### 7. AI Fallback Layer

`ask_ai()` sends the user query plus profile context to OpenAI and asks for:

- Safe advice
- Practical advice
- Short advice

This makes the system more flexible than a purely rule-based chatbot.

## Request Flow Example

### Case 1: BMI Query

```text
User asks: "What is my BMI?"
-> IntentDetector returns "bmi"
-> health_service.calculate_bmi()
-> health_service.bmi_category()
-> formatted response returned to user
```

### Case 2: Diet Query

```text
User asks: "Give me a diet plan"
-> IntentDetector returns "diet"
-> diet_service.generate_meal_plan()
-> meal plan returned to user
```

### Case 3: General Question

```text
User asks: "How can I sleep better?"
-> IntentDetector returns "unknown"
-> ask_ai()
-> OpenAI response returned to user
```

## Current Backend vs Frontend State

The repository contains two parallel experiences:

- Backend CLI agent in `main.py`
- Frontend prototype in `frontend/`

Important note:

- The frontend is currently mock-driven
- It does not call the Python services directly
- There is no API layer yet between `frontend/` and the backend logic

So the architecture is modular, but not yet full-stack integrated.

## Dependencies

From `requirements.txt`:

- `openai`
- `python-dotenv`

## Environment Configuration

The Python backend reads:

```env
OPENAI_API_KEY=your_key_here
```

`main.py` uses `OPENAI_API_KEY`, so the environment file should provide that variable for AI fallback to work.

## How To Run

### Run the Python agent

```bash
python main.py
```

### Open the frontend prototype

Open `frontend/index.html` in a browser or serve it with a local live server.

## Example Interaction

```text
Enter your details
Age: 25
Weight (kg): 70
Height (cm): 175
Goal: fat loss
Diet: vegetarian

HEALTH REPORT
BMI: 22.86 | Category: Normal weight
Calories: 2099

You: workout
Agent: {generated workout plan}
```

## Strengths Of The Current Design

- Clear separation of concerns
- Easy to read and beginner-friendly modules
- Simple controller-based flow
- Good base for adding an API layer later
- Easy to extend with more intents and services

## Current Limitations

- Intent detection is keyword-only
- No persistent database
- No real frontend-backend integration
- No API server such as Flask or FastAPI yet
- Very limited personalization logic
- Safety is basic and not medical-grade

## Suggested Next Architecture Step

If this project grows, the next clean structure would be:

```text
frontend UI
    |
    v
REST API / FastAPI layer
    |
    v
Controller / Orchestration layer
    |
    +--> user service
    +--> health service
    +--> diet service
    +--> fitness service
    +--> tracking service
    |
    v
AI provider layer
```

That would connect the current UI prototype with the existing Python service modules in a scalable way.

## Summary

This project is a modular health assistant with a simple but clean internal structure. The main orchestration happens in `main.py`, the business logic lives in `services/`, and the browser UI in `frontend/` currently acts as a separate prototype. If someone reads the repository for the first time, the best mental model is:

- `main.py` is the controller and runtime
- `services/` is the business logic layer
- `frontend/` is the presentation prototype
- OpenAI is used only when rule-based intent matching cannot answer the question
