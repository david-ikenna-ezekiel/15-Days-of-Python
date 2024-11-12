# Sum of First N Natural numbers

n = int(input("Enter a positive integer: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)

