import sys

def read_input(filepath):
    file_content = None
    try:
        with open(filepath, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File \"{filepath}\" not found. Please check the file path and try again.")
        sys.exit()
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit()
    return file_content