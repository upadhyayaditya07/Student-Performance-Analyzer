class Student:
    """Represents one student's academic record."""

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A+"
        if avg >= 80:
            return "A"
        if avg >= 70:
            return "B"
        if avg >= 60:
            return "C"
        if avg >= 50:
            return "D"
        return "F"

    def __str__(self):
        return (
            f"{self.student_id} | {self.name} | "
            f"Average: {self.average():.2f} | Grade: {self.grade()}"
        )
