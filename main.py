import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

# load the environment variables from the .env file using the dotenv library and read the API key.
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Use the API key to create a new instance of a Gemini client.
client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")

    # command line arguments
    # check required
    if len(sys.argv) < 2:
        print("Error: No argument provided.")
        sys.exit(1)
    
    # discard script name and unpack args
    _, *rest = sys.argv

    prompt = rest[0]
    flags = set(rest[1:])
    verbose = "--verbose" in flags

    # message history
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    # call to gemini 
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    # handle verbose
    if verbose == True:
        print(f"User prompt: {prompt}")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
