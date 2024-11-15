import extract
import transform
import load


def main():
    # File paths
    input_file = "input_data.csv"
    output_file_csv = "cleaned_data.csv"
    output_file_json = "cleaned_data.json"

    # Step 1: Extract data
    data = extract.extract_data(input_file)

    if data is not None:
        # Step 2: Transform data
        cleaned_data = transform.clean_data(data)
        transformed_data = transform.transform_data(cleaned_data)


        # Step 4: Load data
        load.load_data_to_csv(transformed_data, output_file_csv)
        load.load_data_to_json(transformed_data, output_file_json)


if __name__ == "__main__":
    main()
