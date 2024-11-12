

# Creating a dictionary of student grades
grades = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 75, "Science": 95},
    "Charlie": {"Math": 80, "Science": 70}
}

# Accessing grades
print(grades["Alice"]["Math"])  # Output: 90
print(grades["Bob"]["Science"])  # Output: 95

# Adding a new subject for a student
grades["Alice"]["English"] = 88
print(grades["Alice"])

# Modifying an existing grade
grades["Charlie"]["Math"] = 85
print(grades["Charlie"])

# Removing a subject for a student
del grades["Bob"]["Science"]
print(grades["Bob"])
