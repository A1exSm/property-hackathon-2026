from google import genai
from google.genai import types
from gService import get_key

def format_input(message):
    user_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)]
    )
    return user_message

def post_history(client, model_name:str, history) -> str:
    return client.models.generate_content(
        model=model_name,
        contents=history
    ).text

def format_response(text) -> types.Content:
    return types.Content(
        role="model",
        parts=[types.Part.from_text(text=text)],
    )

class Chat:
    def __init__(self):
        api_key = get_key()
        if not api_key:
            raise ValueError("GOOGLE_GEMINI_KEY secret is not set.")
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.1-flash-lite"

        self.history = []

    def send_message(self, message) -> str:
        message = format_input(message)
        self.history.append(message)
        try:
            resp_txt = post_history(self.client, self.model, self.history)

            ai_response = format_response(resp_txt)

            self.history.append(ai_response)

            return resp_txt
        except Exception as e:
            self.history.pop()
            return f"Error communicating with the model: {str(e)}"



