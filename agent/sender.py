import requests
import json
from gService import get_key


URL = "https://iwu38168.live.dynatrace.com/platform/ingest/v1/events"
HEADERS = {
    "Authorization": f"Api-Token {get_key("OPEN_PIPE")}",
    "Content-Type": "application/json"
}


def send_event(payload):
    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=10
        )
        if response.status_code in [200, 201, 202]:
            print("Event sent successfully ", response.text)
        else:
            print(f"Failed to send event. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending event: {e}")

test = {
    "event.provider": "Developer",
    "tests": {
        "state": True,
        "test_unit": 32.5
    }
}

send_event(test)