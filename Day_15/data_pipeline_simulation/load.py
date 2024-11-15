import os
import json

# Load function to save data back to CSV
def load_data_to_csv(data, output_file):
    data.to_csv(output_file, index=False)
    print(f"Data successfully loaded into {output_file}")

# Load function to save data as JSON
def load_data_to_json(data, output_file):
    data.to_json(output_file, orient='records', lines=True)
    print(f"Data successfully loaded into {output_file}")

