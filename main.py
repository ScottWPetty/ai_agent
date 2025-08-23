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

    # accept a command line argument for the prompt.
    # if prompt not provided, print error message and exit with code 1.
    # Add --verbose CL argument
    if len(sys.argv) < 2:
        print("Error: No argument provided.")
        sys.exit(1)
    else:
        prompt = sys.argv[1]
        if sys.argv[2] == "--verbose":
            verbose = True
        else:
            verbose = False

    # LLM's work in a conversation. If we keep track of that history, then with each new prompt, the model
    # can see the entire conversation and respond within the larger context of the conversation.
    # Each message in the conversation has a "role" (message from either the user or the model). While the program will be "one-shot" for now,
    # lets update the code to store a list of messages in the conversation, and pass in the "role" appropriately.
    # Create a new list of types.Content, and set the user's prompt as the only message (for now).
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    # Use the client.models.generate_content() method to get a response from the gemini-2.0-flash-001 model (free tier).
    # The generate_content method returns a GenerateContentResponse object. Print the .txt property of the response
    # to see the models answer. Update your call to use the messages list.
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
