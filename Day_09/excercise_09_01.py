# Function to find the largest number in a list

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Taking a list of numbers as input from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calling the function and displaying the result
print("Largest number:", find_largest(numbers))