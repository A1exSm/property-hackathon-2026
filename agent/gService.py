from typing import Literal
import os
from google.cloud import secretmanager
import hashlib
import secrets
import base64

def __get_env(key: str) -> str:
    project_id = os.getenv('PROJECT_ID')
    if not project_id:
        raise ValueError("project_id environment variable is not set.")
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{key}/versions/1"
    response = client.access_secret_version(request={"name": name})
    base64_value = response.payload.data.decode("UTF-8")  # retrieve key
    if base64_value is None:
        raise ValueError(f"{key} environment variable is not set.")
    return base64_value


def __decode(base64_value:str) -> str:
    decoded_bytes = base64.b64decode(base64_value) # decode from base64 to bytes
    decoded_value = decoded_bytes.decode("utf-8") # decode bytes to string
    return decoded_value


def __compare_hash(env_id:Literal["DYNA","GEMI"], decoded_value:str) -> bool:
    expected_hashes = {
        "DYNA": "b1f0f1b76ec689ff7b28853513b0c51f1b1c0687780b7455302efdd9de9f32e0",
        "GEMI": "37956b5b6c1622b051d6e39f9ea597adcac2b82610b4d28e86eddfcb406162ba"
    }
    value_sha256 = hashlib.sha256(decoded_value.encode('utf-8')).hexdigest()  # compute sha256 hash
    return secrets.compare_digest(value_sha256, expected_hashes[env_id])


ids = {"DYNA":"PLAT_TOKEN","GEMI":"GOOGLE_API_KEY","DB_USER": "DB_USERNAME", "DB_PASS": "DB_PASSWORD", "DB_PORT": "DB_PORT", "DB_HOST": "DB_HOST", }


def get_key(env_id: Literal["DYNA", "GEMI", "DB_USER", "DB_PASS", "DB_PORT", "DB_HOST"]) -> str:
    key = ids.get(env_id)
    if not key:
        raise ValueError(f"Invalid env_id: {env_id}")
    base64_value = __get_env(key)  # retrieve key
    decoded_value = __decode(base64_value)  # decode from base64 to string
    if env_id not in ["DYNA", "GEMI"]:
        return decoded_value
    if not __compare_hash(env_id, decoded_value):
        raise ValueError(f"{key} environment variable does not contain a valid key.")
    return decoded_value
