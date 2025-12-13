import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
import sys

# load the environment variables from the .env file using the dotenv library and read the API key.
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Use the API key to create a new instance of a Gemini client.
client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")

    # command line arguments using argparse
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # message history
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    # call to gemini
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', contents=messages
        )
    except Exception as e:
        print("something went wrong")

    # verify usage_metadata incase of failed api request
    if response.usage_metadata == None:
        raise RuntimeError("failed api request")
    
    # handle verbose
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        print(response.text)
    

if __name__ == "__main__":
    main()
