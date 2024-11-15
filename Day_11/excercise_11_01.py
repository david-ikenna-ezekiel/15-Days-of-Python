# Finding and printing the longest line in a file

def find_longest_line(file_path):
    with open(file_path, "r") as file:
        longest_line = ""
        for line in file:
            if len(line) > len(longest_line):
                longest_line = line
    return longest_line.strip()

file_path = "movie_script.txt"
print("Longest line:", find_longest_line(file_path))