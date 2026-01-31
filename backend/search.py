import os
from google import genai
from google.genai import types  # Import types for configuration
from dotenv import load_dotenv

load_dotenv()

# Initialize without forcing 'v1' to avoid the 400 error
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_travel_json(user_input: dict):
    # Use types.GenerateContentConfig for strict parameter naming
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "name": {"type": "STRING"},
                    "description": {"type": "STRING"},
                    "address": {"type": "STRING"}
                },
                "required": ["name", "description", "address"]
            }
        }
    )

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"Generate 15 travel recommendations for {user_input['destination']} on {user_input['date_of_travel']}.",
        config=config  # Use 'config', not 'generation_config'
    )
    
    return response.text

# Your input data
input_data = {
    "destination": "Porto, Portugal",
    "date_of_travel": "May 9, 2026",
    "address": "130 Waterman St"
}

if __name__ == "__main__":
    print(get_travel_json(input_data))
