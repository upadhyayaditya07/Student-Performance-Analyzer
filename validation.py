def validate_student_id(student_id):
    if not student_id:
        raise ValueError("Student ID cannot be empty.")

def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")

def validate_marks(marks):
    if not marks:
        raise ValueError("At least one subject mark is required.")
    for subject, mark in marks.items():
        if not 0 <= mark <= 100:
            raise ValueError(f"{subject} marks must be between 0 and 100.")
