from pydantic import BaseModel
from typing import List


class RecipeRequest(BaseModel):
    ingredients: List[str]
    goal: str = "balanced"
