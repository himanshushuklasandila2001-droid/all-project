import os
from dotenv import load_dotenv
from mistralai.client import Mistral

# Load environment variables
load_dotenv("api.env")

# Get API key
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("MISTRAL_API_KEY not found in api.env")

# Create client
client = Mistral(api_key=api_key)

print("=== Mistral AI Chatbot ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        print("Bot:", response.choices[0].message.content)
        print()

    except Exception as e:
        print("Error:", e)