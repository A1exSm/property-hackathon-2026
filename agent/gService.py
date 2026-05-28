from typing import Literal
from google.cloud import secretmanager
from dotenv import load_dotenv
import os
import hashlib
import secrets
import base64
#.env
def get_env_key(key_type:Literal["DYNA","GEMI"]) -> str:
    load_dotenv()
    # assert what key to use
    key = "PLAT_TOKEN" if key_type == "DYNA" else "GOOGLE_API_KEY"
    base64_value = os.getenv(key) # retrieve key
    if base64_value is None:
        raise ValueError(f"{key} environment variable is not set.")
    decoded_bytes = base64.b64decode(base64_value) # decode from base64 to bytes
    decoded_value = decoded_bytes.decode("utf-8") # decode bytes to string
    value_sha256 = hashlib.sha256(decoded_value.encode('utf-8')).hexdigest() # compute sha256 hash
    # Compare with sha256 of expected values
    is_valid = (
        secrets.compare_digest(value_sha256, "b1f0f1b76ec689ff7b28853513b0c51f1b1c0687780b7455302efdd9de9f32e0")
    ) if key_type == "DYNA" else (
        secrets.compare_digest(value_sha256, "37956b5b6c1622b051d6e39f9ea597adcac2b82610b4d28e86eddfcb406162ba")
    )
    if not is_valid:
        raise ValueError(f"{key} environment variable does not contain a valid key.")
    return decoded_value
# Google Cloud Secrets
def get_secret_name(secret_id:str) -> str:
    project_id = os.environ.get('project_id')
    if not project_id:
        raise ValueError("project_id environment variable is not set.")
    return f"projects/{project_id}/secrets/{secret_id}/versions/1"

def get_secret(name:str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def get_gem_key() -> str:
    name = get_secret_name('GOOGLE_GEMINI_KEY')
    return get_secret(name)

def get_dyna_key() -> str:
    name = get_secret_name('PLAT_KEY_DYNA')
    return get_secret(name)