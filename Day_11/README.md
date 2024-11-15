# Day 11: File Handling

## Overview
On Day 11, we’ll dive into file handling, which is essential for working with data stored in external files. You’ll learn how to open, read, write, and delete files, as well as explore file methods for controlling how you interact with file content. By the end of this lesson, you’ll be comfortable performing basic file operations in Python.

## Topics Covered
1. **Understanding File Handling**
   - Opening files with `open()` in different modes: read (`'r'`), write (`'w'`), append (`'a'`), and read/write (`'r+'`).
   - Closing files properly to free system resources with `close()`.

2. **Reading and Writing Files**
   - **Reading**: Using `read()`, `readline()`, and `readlines()` to retrieve content from files.
   - **Writing**: Using `write()` and `writelines()` to add text to files.

3. **Using File Methods**
   - **seek()**: Moving the file cursor to a specified position.
   - **tell()**: Getting the current position of the file cursor.
   - **flush()**: Immediately writing content to the file, without waiting for the buffer.


## Practical Examples
- **example_11_01.py** - Copying data from one file to another
- **example_11_02.py** - Counting lines, words, and characters in a file

## Quick Exercise
- **excercise_11_01.py** - Write a Python script that reads a file and prints the longest line in the file.p

## Further Practice
1. Write a list of names to a file, one per line.
2. Use `seek()` to move to the start of a file, then read the first line again.
3. Create a program that logs user actions in a file, appending each action with a timestamp.

## Watch the Lesson
[Watch on YouTube](https://www.youtube.com/sample_link)
