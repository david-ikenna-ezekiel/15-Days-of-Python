import pandas as pd

# Transform function to clean the data
def clean_data(data):
    cleaned_data = data.dropna()
    print("Data cleaning successful. Missing values removed")
    return cleaned_data

# Transform function to perform simple transformations (e.g renaming columns)
def transform_data(data):
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        print("Date transformation successful.")
    return data