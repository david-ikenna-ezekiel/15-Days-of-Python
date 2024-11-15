# Taking a list of numbers as input from the user

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Initializing variables to store the largest and smallest numbers
largest = numbers[0]
smallest = numbers[0]

# Iterating through the list to find the largest and smallest numbers
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number


print("Largest number:", largest)
print("Smallest number:", smallest)

