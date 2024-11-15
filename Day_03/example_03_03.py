
age = int(input("Enter your age: "))
has_permission = input("Do you have permission from your parents? (yes/no): ")
can_drive = age >= 18 or (age>=16 and has_permission.lower() == "yes")
print("Can drive:", can_drive)