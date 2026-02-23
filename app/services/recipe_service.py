import asyncio
from app.services.cache_service import get_cache, set_cache, acquire_lock, release_lock
from app.services.model_service import generate_recipe_from_model
from app.utils.hashing import generate_cache_key
from app.prompts.recipe_prompts import recipe_prompt


async def generate_recipe(request):
    request_dict = request.dict()
    cache_key = generate_cache_key(request_dict)
    lock_key = f"lock:{cache_key}"

    # check cache
    cached = get_cache(cache_key)
    if cached:
        return cached

    # try acquiring lock
    lock_value = acquire_lock(lock_key)

    if lock_value:
        try:
            # double-check cache after acquiring lock
            cached = get_cache(cache_key)
            if cached:
                return cached

            # call LLM
            prompt = recipe_prompt(request.ingredients, request.goal)
            result = await generate_recipe_from_model(prompt)

            # store cache
            set_cache(cache_key, result)

            return result
        finally:
            release_lock(lock_key, lock_value)

    # if lock not acquired - wait and retry cache
    for _ in range(10):
        await asyncio.sleep(1)
        cached = get_cache(cache_key)
        if cached:
            return cached

    return {"error": "Failed to generate recipe. Try again."}
