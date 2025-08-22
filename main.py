import os
from dotenv import load_dotenv
from google import genai
import sys

# load the environment variables from the .env file using the dotenv library and read the API key.
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Use the API key to create a new instance of a Gemini client.
client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")

    # Use the client.models.generate_content() method to get a response from the gemini-2.0-flash-001 model (free tier).
    # The generate_content method returns a GenerateContentResponse object. Print the .txt property of the response
    # to see the models answer.

    # accept a command line argument for the prompt.
    # if prompt not provided, print error message and exit with code 1.
    if len(sys.argv) < 2:
        print("Error: No argument provided.")
        sys.exit(1)
    else:
        prompt = sys.argv[1]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
