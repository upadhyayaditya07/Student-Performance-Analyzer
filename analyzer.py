def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student(students):
    print("\n--- Add Student ---")
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter student name: ").strip()

    subjects = ["Python", "Mathematics", "Problem Solving"]
    marks = {}

    for subject in subjects:
        marks[subject] = get_mark(subject)

    average = calculate_average(list(marks.values()))

    student = {
        "id": student_id,
        "name": name,
        "marks": marks,
        "average": average,
        "grade": get_grade(average),
    }

    students.append(student)
    print("Student added successfully.")


def display_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records available.")
        return

    print(f"{'ID':<12}{'Name':<20}{'Average':<12}{'Grade':<8}")
    print("-" * 52)

    for student in students:
        print(
            f"{student['id']:<12}"
            f"{student['name']:<20}"
            f"{student['average']:<12.2f}"
            f"{student['grade']:<8}"
        )


def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print(f"Name    : {student['name']}")
            print(f"Python  : {student['marks']['Python']:.2f}")
            print(f"Maths   : {student['marks']['Mathematics']:.2f}")
            print(f"Problem : {student['marks']['Problem Solving']:.2f}")
            print(f"Average : {student['average']:.2f}")
            print(f"Grade   : {student['grade']}")
            return

    print("Student not found.")


def calculate_class_statistics(students):
    print("\n--- Class Statistics ---")

    if not students:
        print("No student records available.")
        return

    averages = [student["average"] for student in students]
    class_average = calculate_average(averages)
    highest = max(averages)
    lowest = min(averages)

    print(f"Number of students : {len(students)}")
    print(f"Class average      : {class_average:.2f}")
    print(f"Highest average    : {highest:.2f}")
    print(f"Lowest average     : {lowest:.2f}")


def sort_students_by_average(students):
    print("\n--- Students Sorted by Average ---")

    if not students:
        print("No student records available.")
        return

    # Selection sort: included to demonstrate an algorithm from the
    # problem-solving/array-technique part of the course.
    sorted_students = students.copy()

    for i in range(len(sorted_students) - 1):
        max_index = i

        for j in range(i + 1, len(sorted_students)):
            if sorted_students[j]["average"] > sorted_students[max_index]["average"]:
                max_index = j

        sorted_students[i], sorted_students[max_index] = (
            sorted_students[max_index],
            sorted_students[i],
        )

    for rank, student in enumerate(sorted_students, start=1):
        print(
            f"{rank}. {student['name']} "
            f"({student['id']}) - {student['average']:.2f} - {student['grade']}"
        )


def show_subject_summary(students):
    print("\n--- Subject-wise Summary ---")

    if not students:
        print("No student records available.")
        return

    subjects = ["Python", "Mathematics", "Problem Solving"]

    for subject in subjects:
        marks = [student["marks"][subject] for student in students]
        average = calculate_average(marks)
        highest = max(marks)
        lowest = min(marks)

        print(f"\n{subject}")
        print(f"  Average : {average:.2f}")
        print(f"  Highest : {highest:.2f}")
        print(f"  Lowest  : {lowest:.2f}")


def show_top_performers(students):
    print("\n--- Top Performers ---")

    if not students:
        print("No student records available.")
        return

    averages = [student["average"] for student in students]
    top_average = max(averages)

    top_students = []
    for student in students:
        if student["average"] == top_average:
            top_students.append(student)

    for student in top_students:
        print(
            f"{student['name']} ({student['id']}) "
            f"- Average: {student['average']:.2f}, Grade: {student['grade']}"
        )
