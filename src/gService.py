import os
from google.cloud import secretmanager

def get_key() -> str:
    project_id = os.environ.get('project_id')
    if not project_id:
        raise ValueError("project_id environment variable is not set.")
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/GOOGLE_GEMINI_KEY/versions/1"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")