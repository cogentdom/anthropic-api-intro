# https://platform.claude.com/docs/en/build-with-claude/working-with-messages
import anthropic
from os import getenv
from dotenv import load_dotenv

# Loads variables from the environment
load_dotenv()
open_api_key = getenv("ANTHROPIC_API_KEY")

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message)