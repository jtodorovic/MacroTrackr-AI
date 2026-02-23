from fastapi import APIRouter
from app.schemas.recipe import RecipeRequest
from app.services.recipe_service import generate_recipe

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.post("/generate")
async def generate(request: RecipeRequest):
    return await generate_recipe(request)
