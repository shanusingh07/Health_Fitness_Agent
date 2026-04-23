# 🐛 Known Issues – Health Fitness Agent

## Resolved Issues

### 1. Gemini API Not Working (Day 2)
- **Problem**: `gemini-pro` model deprecated, 404 errors
- **Fix**: Switched to OpenAI (ChatGPT) API
- **Status**: ✅ Resolved

### 2. ModuleNotFoundError on Imports (Day 3)
- **Problem**: Import paths didn't match folder structure
- **Fix**: Corrected import statements to match actual directory layout
- **Status**: ✅ Resolved

### 3. API Key Loading Issue (Day 3)
- **Problem**: `.env` file not loading correctly
- **Fix**: Added `python-dotenv` and `load_dotenv()` call
- **Status**: ✅ Resolved

---

## Current Limitations

### 1. Frontend Not Connected to Backend
- **Description**: Frontend uses mock data, not connected to Python backend yet
- **Workaround**: Frontend simulates responses locally
- **Priority**: 🟡 Medium

### 2. No Chat History Persistence
- **Description**: Chat history is lost when session ends
- **Planned Fix**: Add file-based or database storage
- **Priority**: 🟡 Medium

### 3. Basic Intent Detection
- **Description**: Intent detector uses simple keyword matching
- **Planned Fix**: Integrate NLP or use AI for intent classification
- **Priority**: 🟢 Low

---

## Reporting Issues

If you find a new issue:
1. Document the error message
2. Note the steps to reproduce
3. Add it to this file with status and priority
