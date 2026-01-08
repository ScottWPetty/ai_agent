import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes the data in the 'content' argument to the file whose file path is 'file_path', returns a success string if successful",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Filepath to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="data that is written to the file"
            ),
        },
        required=["file_path", "content"]
    ),
)

def write_file(working_directory, file_path, content):
    try:
        # make sure the file_path is inside the working directory and that it points to a file
        joined = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(joined)
        absolute_working_path = os.path.abspath(working_directory)
        if not absolute_path.startswith(absolute_working_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(absolute_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # make sure parent directories exist
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

        # write content to file
        with open(absolute_path, "w") as f:
            f.write(content)

    except Exception as e:
        print(f"Error: {e}")
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    

    