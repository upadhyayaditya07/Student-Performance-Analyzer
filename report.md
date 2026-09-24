# Project Report
## Student Performance Analyzer

### 1. Introduction
Student Performance Analyzer is a command-line Python program developed for CSE1021 - Introduction to Problem Solving and Programming. The application stores student marks and performs basic academic analysis.

### 2. Problem Statement
Managing marks for multiple students manually makes it difficult to calculate averages, compare performance, search records, and generate subject-wise statistics. The proposed program automates these basic tasks through a simple menu-driven Python application.

### 3. Objectives
- Store student information and marks.
- Calculate individual averages and grades.
- Search student records.
- Calculate class-level statistics.
- Sort students according to average marks.
- Generate subject-wise statistics.
- Demonstrate fundamental problem-solving and Python programming concepts.

### 4. Scope
The application is intended as a small command-line academic record analysis tool. It focuses on demonstrating the programming and algorithmic concepts covered in CSE1021 rather than providing a complete database or graphical management system.

### 5. Technologies Used
- Python 3
- Command-line interface
- No external libraries

### 6. Concepts Used
- Problem decomposition
- Functions
- Variables and expressions
- Conditional statements
- Iteration
- Lists
- Dictionaries
- Searching
- Counting and summation
- Maximum and minimum
- Selection Sort
- Input validation

### 7. System Design
The program is divided into two Python files.

`main.py`:
- Displays the menu.
- Accepts the user's choice.
- Calls the appropriate function.

`analyzer.py`:
- Contains the application logic.
- Handles student records.
- Performs calculations.
- Performs searching and sorting.
- Generates summaries.

### 8. Data Representation
Each student is represented using a dictionary:

```text
{
    "id": student ID,
    "name": student name,
    "marks": {
        "Python": marks,
        "Mathematics": marks,
        "Problem Solving": marks
    },
    "average": calculated average,
    "grade": calculated grade
}
```

All student dictionaries are stored in a list.

### 9. Algorithms

#### 9.1 Average
The average is calculated as:

Average = Sum of marks / Number of subjects

#### 9.2 Grade
The program uses conditional statements to assign grades according to the calculated average.

#### 9.3 Search
The program traverses the student list and compares each student's ID with the entered ID.

#### 9.4 Selection Sort
Students are sorted in descending order of average marks using Selection Sort.

### 10. Time Complexity
- Student search: O(n)
- Class statistics: O(n)
- Subject summary: O(n)
- Selection Sort: O(n²)

Here, n represents the number of student records.

### 11. Input Validation
The program checks:
- Marks must be numeric.
- Marks must be between 0 and 100.
- Student IDs must be unique.

### 12. Testing

| Test Case | Input/Action | Expected Result |
|---|---|---|
| 1 | Add valid student | Student is added |
| 2 | Enter marks above 100 | Error message and re-entry |
| 3 | Enter negative marks | Error message and re-entry |
| 4 | Add duplicate ID | Record is rejected |
| 5 | Search existing ID | Student details displayed |
| 6 | Search unknown ID | "Student not found" |
| 7 | View statistics with records | Class statistics displayed |
| 8 | Sort with records | Students shown in descending average |
| 9 | Select an option before adding records | Program reports no records |
| 10 | Exit | Program terminates |

### 13. Limitations
- Data is stored only during program execution.
- There is no database or permanent file storage.
- The program uses a fixed set of three subjects.
- It is designed as a command-line application.

### 14. Future Scope
Possible future improvements include file-based storage, configurable subjects, a graphical interface, and database integration. These are outside the current scope of the CSE1021 project.

### 15. Conclusion
The Student Performance Analyzer demonstrates how a real-world record-analysis problem can be decomposed into smaller programming tasks. The project applies Python functions, conditionals, loops, lists, dictionaries, searching, calculations, and a sorting algorithm in a single command-line application.
