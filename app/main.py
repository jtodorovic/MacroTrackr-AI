from fastapi import FastAPI
from app.api.recipe import router as recipe_router

app = FastAPI(title="Recipe Generator API")

app.include_router(recipe_router)


@app.get("/health")
async def health():
    return {"status": "ok"}
