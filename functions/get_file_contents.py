import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_contents = types.FunctionDeclaration(
    name="get_file_contents",
    description="Reads and returns a string containing the contents of the file whose path is 'file_path'. The returned string contains up to 1000 chars",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Filepath to get the contents from, relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)

def get_file_content(working_directory, file_path):
    try:
        joined = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(joined)
        absolute_working_path = os.path.abspath(working_directory)
        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if not absolute_path.startswith(absolute_working_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
    
    try:
        with open(absolute_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string = file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error: {e}"

    return file_content_string