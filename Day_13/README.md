# Day 13: Error Handling

## Overview
On Day 13, we’ll cover error handling, a crucial concept for writing robust Python programs. You’ll learn how to manage errors gracefully using `try`, `except`, `else`, and `finally` blocks, handle specific exceptions, and even create your own custom exceptions. By the end of this lesson, you’ll be equipped to handle unexpected errors and make your code more reliable.

## Topics Covered
1. **Understanding Error Handling with `try`, `except`, `else`, and `finally` Blocks**
   - **try**: Wraps the code you want to monitor for errors.
   - **except**: Catches and handles exceptions if they occur in the `try` block.
   - **else**: Executes code if no exceptions are raised in the `try` block.
   - **finally**: Always executes code after `try` and `except` blocks, useful for cleanup tasks.

2. **Catching Specific Exceptions and Raising Exceptions**
   - Catching specific exceptions (e.g., `ValueError`, `TypeError`) to handle different error types appropriately.
   - **Raising exceptions**: Using `raise` to trigger exceptions intentionally, which is useful for input validation and enforcing rules.

3. **Creating Custom Exceptions**
   - Defining custom exception classes by subclassing Python’s built-in `Exception` class.
   - Using custom exceptions to add descriptive error handling for application-specific situations.


## Practical Examples
- **example_13_01.py** - Function to read from a file and handle possible exceptions

## Quick Exercise
- **excercise_13_01.py** - Write a Python script that reads a list of numbers from a file, calculates the average, and handles any potential errors (e.g., file not found, invalid data).

## Further Practice
1. Write a custom exception for validating that a string contains only alphabetical characters.
2. Use `try`, `except`, and `finally` in a program that prompts for user input and cleans up resources afterward.

## Watch the Lesson
[Watch on YouTube](https://www.youtube.com/sample_link)