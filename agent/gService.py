import os
from google.cloud import secretmanager
from dotenv import load_dotenv

def get_dyna_key_env() -> str | None:
    load_dotenv()
    return os.getenv("PLAT_KEY")

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