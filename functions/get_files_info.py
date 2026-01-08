import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    
    # check if directory is within the bounds of the working directory
    try:
        joined = os.path.join(working_directory, directory)
        absolute_path = os.path.abspath(joined)
        absolute_working_path = os.path.abspath(working_directory)
        if not os.path.isdir(absolute_path):
            return f'Error: "{directory}" is not a directory'

        if not absolute_path.startswith(absolute_working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return e
    
    # build and return a string representing the contents of the directory
    try:
        contents_string = ""
        contents_list = os.listdir(absolute_path)
        for item in contents_list:
            new_path = os.path.join(absolute_path, item)
            file_size = os.path.getsize(new_path)
            if os.path.isdir(new_path):
                contents_string = contents_string + f"- {item}: file_size={file_size} bytes, is_dir=True\n"
            if os.path.isfile(new_path):
                contents_string = contents_string + f"- {item}: file_size={file_size} bytes, is_dir=False\n"
        return contents_string[:-1]
    except Exception as e:
        return e
