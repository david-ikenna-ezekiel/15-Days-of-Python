# Function returning multiple values using a tuple

def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count != 0 else 0
    return total, count, average  # Returns a tuple

numbers = [10, 20, 30, 40, 50]
total, count, average = get_stats(numbers)
print(f"Total: {total}, Count: {count}, Average: {average}")
