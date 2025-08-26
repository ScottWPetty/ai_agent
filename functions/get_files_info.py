import os

def get_files_info(working_directory, directory="."):
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    joined = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(joined)
    absolute_working_path = os.path.abspath(working_directory)

    if not absolute_path.startswith(absolute_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted orking directory'
    
    
