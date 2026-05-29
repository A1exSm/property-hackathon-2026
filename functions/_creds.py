from typing import Literal
import os
import base64


def __get_env(key: str) -> str:
    base64_value = os.getenv(key)  # retrieve key
    if base64_value is None:
        raise ValueError(f"{key} environment variable is not set.")
    return base64_value


def __decode(base64_value: str) -> str:
    decoded_bytes = base64.b64decode(base64_value)  # decode from base64 to bytes
    decoded_value = decoded_bytes.decode("utf-8")  # decode bytes to string
    return decoded_value


ids = {"DB_USER": "DB_USERNAME", "DB_PASS": "DB_PASSWORD","DB_PORT": "DB_PORT", "DB_HOST": "DB_HOST", }


def get_key(env_id: Literal["DYNA", "GEMI", "DB_USER", "DB_PASS", "DB_PORT", "DB_HOST"]) -> str:
    key = ids.get(env_id)
    if not key:
        raise ValueError(f"Invalid env_id: {env_id}")
    base64_value = __get_env(key)  # retrieve key
    decoded_value = __decode(base64_value)  # decode from base64 to string
    return decoded_value
