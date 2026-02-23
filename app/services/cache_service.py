import json
import uuid
from app.core.redis_client import redis_client
from app.core.config import CACHE_TTL, LOCK_TTL


def get_cache(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def set_cache(key: str, value: dict):
    redis_client.set(key, json.dumps(value), ex=CACHE_TTL)


def acquire_lock(lock_key: str):
    lock_value = str(uuid.uuid4())
    acquired = redis_client.set(lock_key, lock_value, nx=True, ex=LOCK_TTL)
    if acquired:
        return lock_value
    return None


def release_lock(lock_key: str, lock_value: str):
    # safe unlock
    script = """
    if redis.call("get", KEYS[1]) == ARGV[1] then
        return redis.call("del", KEYS[1])
    else
        return 0
    end
    """
    redis_client.eval(script, 1, lock_key, lock_value)
