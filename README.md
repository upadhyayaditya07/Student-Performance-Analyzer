# Student Performance Analyzer

A modular, command-line Python project for **CSE1021 / Python Essentials** that demonstrates problem solving, functions, lists, dictionaries, conditionals, loops, searching, counting/summation, max/min, and selection sort.

## Features
- Add and validate student records
- Prevent duplicate student IDs
- Search students using linear search
- Calculate class statistics
- Calculate subject-wise statistics
- Assign grades
- Rank students using selection sort
- Display top performers
- Run completely from a terminal

## Project Structure
- `main.py` — command-line user interface and application entry point
- `student.py` — Student data model and grade/average logic
- `student_manager.py` — record management
- `validation.py` — input validation
- `search.py` — linear search algorithm
- `sorting.py` — selection sort algorithm
- `statistics.py` — class and subject statistics
- `reporting.py` — formatted terminal reports
- `statement.md` — project statement, scope, users, and features
- `requirements.txt` — dependency information
- `tests/test_project.py` — basic validation tests

## Environment Setup
1. Install Python 3.9 or later.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. No third-party packages are required.

## Run
```bash
python main.py
```

On some systems:
```bash
python3 main.py
```

## Testing
Run:
```bash
python -m unittest discover -s tests -v
```

## Example Workflow
1. Choose `1` to add students.
2. Enter marks from 0 to 100.
3. Use `2` to display records.
4. Use `3` to search by ID.
5. Use `4` for class statistics.
6. Use `5` for selection-sort ranking.
7. Use `6` for subject-wise analysis.
8. Use `7` for top performers.
9. Choose `8` to exit.

## Course Concepts Demonstrated
Problem decomposition, functions, variables and data types, lists, dictionaries, conditionals, loops, input/output, searching, counting and summation, max/min, selection sort, modular programming, validation, and basic complexity analysis.

## Complexity
- Linear search: O(n)
- Selection sort: O(n²)
- Class statistics: O(n)
- Subject statistics: O(n × s), where `s` is the number of subjects
