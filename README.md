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

mistralai/Mistral-7B-Instruct

- Instruction-tuned large language model from Mistral AI.

Chosen because:

- Strong instruction-following performance

- Significantly more capable than small T5-class models

- High-quality natural language generation

- Good reasoning ability for structured outputs (e.g., recipes, formatting, constraints)

- Optimized transformer architecture with efficient attention

- Open-weight model suitable for self-hosted deployments

- Works well with quantization (4-bit / 8-bit) for reduced memory usage

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
