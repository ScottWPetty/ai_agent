import os, subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="calls a subprocess to run the python file given by file_path with the arguments given by args (default for args is None)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="python script that is commanded to run by a subprocess",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="arguments that are passed to the python script that runs"
                ),
                description="array that contains arguments to be passed to the python script that runs"
            ),
        },
        required=["file_path"]
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        # make sure filepath is inside the working directory
        joined = os.path.join(working_directory, file_path)
        absolute_file_path = os.path.abspath(joined)
        absolute_working_path = os.path.abspath(working_directory)
        if not absolute_file_path.startswith(absolute_working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # make sure the filepath is a file
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # check if file ends with .py
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

    except Exception as e:
        return f"Error: {e}"

    try:
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)
    
        process_obj = subprocess.run(command, capture_output=True, text=True, timeout=30)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    output_string = ""
    if process_obj.returncode != 0:
        output_string += f"Process exited with code {process_obj.returncode}\n"
    
    if not process_obj.stdout and not process_obj.stderr:
        output_string += f"No output produced"
    else:
        output_string += f"STDOUT: {process_obj.stdout}\nSTDERR: {process_obj.stderr}\n"
    
    return output_string
    