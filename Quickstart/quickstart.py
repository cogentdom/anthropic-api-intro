# https://platform.claude.com/docs/en/get-started#python
import anthropic
from os import getenv
from dotenv import load_dotenv

# Loads variables from the environment
load_dotenv()
open_api_key = getenv("ANTHROPIC_API_KEY")


client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
        }
    ],
)
print(message.content)