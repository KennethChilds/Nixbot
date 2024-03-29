#!/usr/bin/env python3
import anthropic
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=ANTHROPIC_API_KEY,
)

try:
    while True:
        user_input = input("\n> ")

        with client.messages.stream(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.0,
            system="""
                *nixbot is an AI-powered assistant designed to guide users 
                in customizing their operating system environments for enhanced 
                productivity and aesthetic appeal.
                
                Try to give the easiest and most direct way to achieve the user's goal, 
                such as telling users how to install arch linux via archinstall.
                
                Keep information VERY concise and to the point.
            """,
            messages=[
                {"role": "user", "content": f"{user_input}"}
            ]
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
except KeyboardInterrupt:
    print("\nExited nixbot")

