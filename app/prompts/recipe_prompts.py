def recipe_prompt(ingredients, goal="balanced"):
    return f"""
    You are a cooking assistant.

    Given these ingredients: {ingredients} and goal: {goal}, generate a recipe that will use all of the ingredients to achieve {goal} type of meal.

    Respond with a single valid JSON object.

    The JSON must contain:
    - title (string)
    - servings (number)
    - ingredients (array of strings)
    - instructions (array of strings)

    Do not include explanations.
    Do not include markdown.
    Do not wrap the JSON in another object.
    Output must start with {{ and end with }}.
    Each instruction must be a separate string element in the array and must not contain markdown.

    JSON:
    """
