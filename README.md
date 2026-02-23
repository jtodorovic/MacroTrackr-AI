# MacroTrackr AI – Recipe Generation Service

AI-powered microservice that generates simple, goal-oriented recipes from user-provided ingredients.

Built as an extension of the MacroTrackr project.

---

## Features

- Generate recipes from available ingredients
- Supports fitness goals:
  - balanced
  - high-protein
  - low-calorie
  - bulking
- Returns:
  - Recipe title
  - Ingredients
  - Instructions
  - Estimated macros (calories, protein, carbs, fat)

---

## Model

Uses:

google/flan-t5-small

Instruction-tuned transformer model from Hugging Face.

Chosen because:

- CPU-friendly
- Low memory usage
- Fast inference
- Good instruction-following capability

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd macrotrackr-ai
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Service

```bash
uvicorn app.main:app --reload
```

Service will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Example Request

POST `/generate-recipe`

```json
{
  "ingredients": "eggs, chicken, spinach",
  "goal": "high-protein"
}
```

---

## System Requirements

- Ubuntu 22.04 (tested)
- 16GB RAM recommended
- CPU-only (no GPU required)

Typical performance:

- Model load time: ~10–15s (first run)
- Generation time: ~1–3s

---

## Future Improvements

- Structured JSON output
- Caching layer
- Macro calculation validation
- Docker support
- Deployment to VPS
- Integration with MacroTrackr backend

---
