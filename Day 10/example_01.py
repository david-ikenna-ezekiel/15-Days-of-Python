# Palindrome Checker

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is palindrome.")
else:
    print(f"'{word}' is not palindrome.")

