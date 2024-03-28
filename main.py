# Load environment variables
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# CLAUDE 3
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=ANTHROPIC_API_KEY,
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": "How are you today?"}
    ]
)

print(message.content)