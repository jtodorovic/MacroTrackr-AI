from llama_cpp import Llama
import json

llm = Llama(
    model_path="./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
)


async def generate_recipe_from_model(prompt: str):

    output = llm(prompt, max_tokens=300, temperature=0.8, top_p=0.95)

    result = output["choices"][0]["text"]

    start = result.find("{")
    end = result.rfind("}") + 1
    json_str = result[start:end]

    parsed = json.loads(json_str)

    return parsed
