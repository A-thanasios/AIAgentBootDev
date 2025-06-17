import os
import subprocess

def run_python_file(working_directory, file_path):
    



    working_directory_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    file_path = abs_file_path
    


    try:
        result = subprocess.run(['python', file_path], 
                                timeout=1800, capture_output=True,
                                text=True, check=True)
        
        result_string =  f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
        if result.returncode != 0:
            result_string += f'\nProcess exited with code {result.returncode}'
        if result_string.strip():
            return result_string
        else:
            return f'No output produced.'
    
    except subprocess.CalledProcessError as e:
        return f'Error: Script execution failed with error: {e.stderr.strip()}'
    except Exception as e:
        return f'Error: An unexpected error occurred while running "{file_path}": {str(e)}'