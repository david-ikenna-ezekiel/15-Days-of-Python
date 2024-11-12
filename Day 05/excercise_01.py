# Taking a tuple of numbers as input from the user

numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

print(numbers)

# Finding the smallest and largest numbers

smallest = min(numbers)
largest = max(numbers)

print("Smallest number:", smallest)
print("Largest number", largest)