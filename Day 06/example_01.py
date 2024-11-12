# Creating a phonebook dictionary
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Adding a new contact
phonebook["David"] = "444-444-4444"
print(phonebook)

# Modifying an existing contact
phonebook["Alice"] = "111-111-1111"
print(phonebook)

# Removing a contact
del phonebook["Charlie"]
print(phonebook)

# Searching for a contact
contact = phonebook.get("Bob", "Contact not found")
print(contact)
