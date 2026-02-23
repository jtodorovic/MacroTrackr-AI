import json
import hashlib


def normalize_request(data: dict) -> dict:
    return {
        "ingredients": sorted([i.strip().lower() for i in data["ingredients"]]),
        "goal": data.get("goal", "balanced").strip().lower(),
    }


def generate_cache_key(request_data: dict) -> str:
    normalized_data = normalize_request(request_data)
    normalized_json = json.dumps(normalized_data, sort_keys=True)
    return "recipe:" + hashlib.sha256(normalized_json.encode()).hexdigest()
