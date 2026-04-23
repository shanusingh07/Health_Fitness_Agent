# 📚 Research – Health Fitness Agent

## Architecture Research

### Monorepo Microservices Pattern
- **Decision**: Use a single `services/` folder with individual service files
- **Reason**: Simpler structure for a Python CLI agent, avoids unnecessary folder nesting
- **Reference**: [cli-agent](https://github.com/manipalsanyam/cli-agent) by manipalsanyam

### Agent Flow Pattern
```
User Input → Intent Classification → Service Execution → Response Generation
```

This is a standard agentic pipeline where:
1. User provides natural language input
2. Intent detector classifies the query
3. Appropriate service handles the request
4. Response is generated (rule-based or AI-powered)

---

## AI Integration Research

### Gemini API (Attempted - Day 2)
- Tried `gemini-pro` and `gemini-1.5-flash` models
- Faced 404 errors due to API version mismatches
- **Result**: Abandoned in favor of OpenAI

### OpenAI API (Current - Day 3+)
- Using `gpt-5-mini` model
- Works well for health/fitness queries
- Provides fallback for unknown intents
- **Result**: Successfully integrated

---

## BMI Calculation Formula
- **Formula**: `weight(kg) / (height(m))²`
- **Categories**:
  - < 18.5 → Underweight
  - 18.5 - 24.9 → Normal weight
  - 25.0 - 29.9 → Overweight
  - ≥ 30.0 → Obese

## Calorie Estimation
- **Method**: Mifflin-St Jeor Equation
- **Formula**: `BMR = 10 × weight + 6.25 × height - 5 × age + 5`
- **Activity Multiplier**: 1.55 (moderate activity)
- **Goal Adjustments**:
  - Fat loss: -500 kcal
  - Muscle gain: +300 kcal
  - Maintenance: no change

---

## Future Research Topics
- [ ] NLP-based intent detection (spaCy / transformers)
- [ ] Voice interaction (speech-to-text)
- [ ] Database integration for user history
- [ ] REST API for frontend-backend connection
