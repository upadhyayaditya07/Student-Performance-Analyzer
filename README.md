# Student Performance Analyzer

## Course
CSE1021 - Introduction to Problem Solving and Programming

## Project Overview
Student Performance Analyzer is a command-line Python application for storing and analyzing student marks in three subjects: Python, Mathematics, and Problem Solving.

The program demonstrates problem-solving techniques, functions, conditional statements, loops, lists, dictionaries, searching, and a manual sorting algorithm.

## Features
1. Add a student record
2. Validate marks between 0 and 100
3. Prevent duplicate student IDs
4. Display all student records
5. Search for a student by ID
6. Calculate class statistics
7. Sort students by average using Selection Sort
8. Generate subject-wise statistics
9. Identify top-performing student(s)
10. Assign grades based on average marks

## Requirements
- Python 3.8 or later
- No external Python packages are required

## Project Structure
```text
Student-Performance-Analyzer/
├── main.py
├── analyzer.py
├── README.md
└── report.md
```

## How to Run

### 1. Install Python
Install Python 3.8 or later and verify it from a terminal:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### 2. Download or clone the repository
Open a terminal in the project directory.

### 3. Run the program
```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

### 4. Use the menu
Choose an option from 1 to 8 and follow the prompts.

## Concepts Demonstrated
- Algorithmic problem solving
- Top-down decomposition into functions
- Variables and expressions
- Input and output
- `if`, `elif`, and `else`
- `for` and `while` loops
- `break` and `return`
- Functions and parameters
- Lists
- Dictionaries
- Searching
- Array/list traversal
- Selection Sort
- Counting and summation
- Maximum and minimum
- Average calculation
- Basic input validation

## Algorithm: Selection Sort
The "Sort students by average" option uses Selection Sort rather than Python's built-in `sort()` function.

For each position:
1. Assume the current position contains the largest remaining average.
2. Compare it with all later records.
3. Find the student with the highest remaining average.
4. Swap the records.
5. Continue until the list is ordered.

Time complexity: O(n²), where n is the number of students.

## Example
```text
===== STUDENT PERFORMANCE ANALYZER =====
1. Add student
2. Display all students
3. Search student
4. Class statistics
5. Sort students by average
6. Subject-wise summary
7. Show top performers
8. Exit
```

## Notes
This is a terminal-based project and does not require a graphical user interface or external libraries.
