import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from config import model_name
from call_function import available_functions

# load the environment variables from the .env file using the dotenv library and read the API key.
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Use the API key to create a new instance of a Gemini client.
client = genai.Client(api_key=api_key)

def main():
    # print("Hello from ai-agent!")     # boots did not like this. Not sure about removing it yet.

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
    response = None

    try:
        response = client.models.generate_content(
            model=model_name, contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
            )
    except Exception as e:
        print("something went wrong: ", e)
    
    if response == None:
        print("No response")
        return
    
    # verify usage_metadata incase of failed api request
    if response.usage_metadata == None:
        raise RuntimeError("failed api request")
    
    # check for function call objects
    function_calls = response.function_calls

    # handle verbose
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if function_calls:
            for function_call in function_calls:
                if function_call.name != None:
                    print(f"Calling function: {function_call.name}({function_call.args})")
        else:
            print(response.text)

    else:
        if function_calls:
            for function_call in function_calls:
                if function_call.name != None:
                    print(f"Calling function: {function_call.name}({function_call.args})")
        else:
            print(response.text)

    
if __name__ == "__main__":
    main()
