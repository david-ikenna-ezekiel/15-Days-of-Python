# Finding the Largest and Smallest numbers

# Taking a list of numbers as input from the user
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Finding the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)
