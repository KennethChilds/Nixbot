# Load environment variables
#import os
#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())
#ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# CLAUDE 3
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
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