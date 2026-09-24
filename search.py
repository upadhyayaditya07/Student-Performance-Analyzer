def linear_search(students, student_id):
    """Return a student with the requested ID using linear search."""
    for student in students:
        if student.student_id == student_id:
            return student
    return None
