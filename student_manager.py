from student import Student
from validation import validate_student_id, validate_name, validate_marks
from search import linear_search
from sorting import selection_sort_by_average

class StudentManager:
    """Coordinates student records and analysis operations."""

    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, marks):
        validate_student_id(student_id)
        validate_name(name)
        validate_marks(marks)
        if self.search_student(student_id):
            raise ValueError("Student ID already exists.")
        self.students.append(Student(student_id, name, marks))

    def search_student(self, student_id):
        return linear_search(self.students, student_id)

    def sort_by_average(self):
        return selection_sort_by_average(self.students)

    def top_performers(self, count=3):
        return self.sort_by_average()[:count]
