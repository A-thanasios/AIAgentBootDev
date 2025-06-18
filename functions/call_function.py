from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


working_directory = "./calculator"

def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name} {working_directory}, {function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")


    match function_call.name:

        case "get_files_info":
            function_result = get_files_info(working_directory, function_call.args['file_path'])
        
        case "get_file_content":
            function_result = get_file_content(working_directory, function_call.args['file_path'])
        
        case "run_python_file":
            function_result = run_python_file(working_directory, function_call.args['file_path'])
        
        case "write_file":
            function_result = write_file(working_directory, function_call.args['file_path'], function_call.args['content'])
        
        case _:
            return types.Content(
                        role="tool",
                        parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={"error": f"Unknown function: {function_call.name}"},
                    )
                ],
            )
        
    return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={"result": function_result},
                    )
                ],
            )
    