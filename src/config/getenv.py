import os

def get_env(key: str) -> str | None:
    return os.getenv(key)