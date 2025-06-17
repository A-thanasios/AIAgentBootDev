import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    working_directory_path = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path.startswith(working_directory_path):
         return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_path, 'r') as f:
            
            content = f.read()
            
            if len(content) > MAX_CHARS:
                return f'{content[:MAX_CHARS]} [...File "{file_path}" truncated at 10000 characters]'
            
            return content

    except Exception as e:
        return f'Error: An unexpected error occurred while reading "{file_path}": {str(e)}'