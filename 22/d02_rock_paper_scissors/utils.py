def readInStrategy(fileName):
    file_contents = None
    try:
        with open(fileName, 'r') as file:
            # Read the contents of the file as a string
            file_contents = file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return file_contents