import sys
def readInput(filepath):
    file_contents = None
    try:
        with open(filepath, 'r') as file:
            # Read the contents of the file as a string
            file_contents = file.read()
    except FileNotFoundError:
        print(f"File \"{filepath}\" not found. Please check the file path and try again.")
        sys.exit()
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit()
    return file_contents