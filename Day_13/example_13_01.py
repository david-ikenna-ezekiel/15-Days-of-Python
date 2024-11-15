# Function to read from a file and handle possible exceptions

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        print(f"File not Found: {e}")
    except PermissionError as e:
        print(f"Permission Denied; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_file("nonexistent_file.txt")