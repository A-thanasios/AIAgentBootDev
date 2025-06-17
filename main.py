import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function

def main(*args):
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    verbose = "--verbose" in sys.argv

    user_prompt = sys.argv[1]
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. 
You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    schema_get_files_info = get_schema(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        working_directory="directory"
    )
    schema_get_file_content = get_schema(
        name="get_file_content",
        description="Retrieves the content of a file in the specified file_path, constrained to the working directory.",
        working_directory="directory"
    )
    schema_run_python_file = get_schema(
        name="run_python_file",
        description="Executes a Python file in the specified file_path, constrained to the working directory.",
        working_directory="directory"
    )

    schema_write_file = get_schema(
        name="write_file",
        description="Writes content to a file in the specified file_path as file_path, constrained to the working directory, specify content as content: 'your content here'.",
        working_directory="directory"
    )



    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    

    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize the Gemini AI client with the API key
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]), 
            ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", 
                                            contents=messages,
                                            config=types.GenerateContentConfig(
                                                tools=[available_functions],
                                                system_instruction=system_prompt
                                                )
                                            )
    
    function_calls = response.function_calls

    if function_calls:
        for function in function_calls:
            try:
                if verbose:
                    print(f'-> {call_function(function, verbose).parts[0].function_response.response}')
            except Exception as e:
                print(f"Error calling function {function.name}: {e}")
    
    else:
        print(response.text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def get_schema(name, description, working_directory):
    schema_get_files_info = types.FunctionDeclaration(
        name=name,
        description=description,
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                working_directory: types.Schema(
                    type=types.Type.STRING,
                    description=description + " (relative to the working directory)",
                ),
            },
        ),
    )
    
    return schema_get_files_info

    

if __name__ == "__main__":
    main()