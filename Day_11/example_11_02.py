# counting lines, words, and characters in a file

def count_file_content(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count

file_path = "movie_script.txt"
lines, words, chars = count_file_content(file_path)
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")