# copying content from one file to another

with open("movie_script.txt", "r") as source_file:
    with open("movie_script_destination", "w") as destination_file:
        for line in source_file:
            destination_file.write(line)