# Reading numbers from a file and calculating the average
def read_numbers(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [float(line.strip()) for line in file]
        if not numbers:
            raise ValueError("No numbers in file.")
        return numbers
    except FileNotFoundError:
        print("The file was not found.")
        return []
    except ValueError as e:
        print(e)
        return []

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

file_path = "numbers.txt"
numbers = read_numbers(file_path)
average = calculate_average(numbers)
if average is not None:
    print(f"The average is {average}")
else:
    print("No valid numbers to calculate the average.")
