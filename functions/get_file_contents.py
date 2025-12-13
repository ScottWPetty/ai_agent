import os

def get_file_content(working_directory, file_path):
    joined = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(joined)
    