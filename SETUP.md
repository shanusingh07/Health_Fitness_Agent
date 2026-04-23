# 🔧 Setup Guide – Health Fitness Agent

## Prerequisites

* Python 3.8 or higher
* pip (Python package manager)
* OpenAI API key

---

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Health_Fitness_agent.git
cd Health_Fitness_agent
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
copy .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-key-here
```

### 6. Run the Agent

```bash
python main.py
```

---

## Frontend Setup

The frontend is a static HTML/CSS/JS application located in the `frontend/` folder.

1. Open `frontend/index.html` in your browser
2. Or use a live server extension in VS Code

---

## Troubleshooting

* **ModuleNotFoundError**: Make sure virtual environment is activated
* **API Key Error**: Verify `.env` file has correct OpenAI key
* **Import Errors**: Run from the project root directory (`Health_Fitness_agent/`)
