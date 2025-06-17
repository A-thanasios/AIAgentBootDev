import os

def get_files_info(working_directory, directory=None):
    working_directory_items = os.listdir(working_directory)
    
    if not directory in working_directory_items and not directory == ".":
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    directory = os.path.join(working_directory, directory)
    print(directory)
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    try:
        content = os.listdir(directory)
        string = ''

        for item in content:
            item_path = os.path.join(directory, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            string += f'- {item}: file_size={file_size} bytes, is_dir={is_dir}\n'

        return string.strip() if string else f'No files found in "{directory}"'

    
    except Exception as e:
        return f'Error: An unexpected error occurred while listing "{directory}": {str(e)}'
    
