# Day 15: Project Day

## Overview
On Day 15, we’ll bring together everything you’ve learned in this series by working on two practical projects. These projects will give you hands-on experience with Python’s core concepts, including data handling, file management, and modular coding. Today, we’ll be building a **To-Do List App** and a **CSV Data Pipeline Simulation**.

## Project 1: To-Do List App

### Project Overview
The **To-Do List App** is a simple command-line application where users can add, view, mark, and delete tasks. This project uses concepts such as file handling, data structures (lists and dictionaries), and functions to create a functional task management app.

### Features
- **Add tasks**: Allows the user to create new tasks.
- **View tasks**: Displays all tasks with unique indexes.
- **Mark tasks as complete**: Allows users to mark tasks as completed.
- **Delete tasks**: Enables users to delete tasks.
- **Save to file**: Tasks are saved to a file (`tasks.json`) for persistence.

### Code Structure
- **`todo_functions.py`**: Contains functions to handle adding, viewing, completing, and deleting tasks.
- **`main.py`**: The main script where the user interacts with the to-do list app.

### Quick Example
1. Run `main.py` to start the app.
2. Follow the menu prompts to add, view, complete, or delete tasks.
3. Exit the app to save changes.

## Project 2: CSV Data Pipeline Simulation

### Project Overview
The **CSV Data Pipeline Simulation** is a simple ETL (Extract, Transform, Load) pipeline that simulates loading data from a CSV file, processing the data, and saving the results to a new file. This project introduces data engineering concepts using Python, focusing on reading, transforming, and writing data.

### Features
- **Data Loading**: Reads data from a CSV file.
- **Data Transformation**: Performs operations on data, such as filtering or modifying specific fields.
- **Data Saving**: Writes transformed data to a new CSV file.

### Code Structure
- **`data_pipeline.py`**: Contains functions to load, process, and save CSV data.
- **`transformations.py`**: A module with transformation functions.
- **`main_pipeline.py`**: The main script where the pipeline is executed end-to-end.

### Quick Example
1. Run `main_pipeline.py` to start the pipeline.
2. The script reads data from `input_data.csv`, processes it, and writes the transformed data to `output_data.csv`.

## Tools and Libraries
- **Built-in libraries**: `os`, `json`, `csv`
- **External libraries** (if any): Install via `pip` as needed.

## Future Enhancements
- **Error Handling**: Add `try-except` blocks to handle file-related errors, such as missing files.
- **User Interface**: Create a simple GUI using `tkinter` for the To-Do List App.
- **Data Validation**: Improve data validation and error handling in the CSV pipeline to manage malformed data.
- **Modularization**: Further modularize the code for scalability and maintenance.

## Watch the Lesson
[Watch on YouTube](https://www.youtube.com/sample_link)

