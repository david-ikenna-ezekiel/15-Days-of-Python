import pandas as pd

# Extract function to load data from a CSV file
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data extraction successful.")
        return data
    except FileNotFoundError:
        print("Error: The file was not found")
        return None